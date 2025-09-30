from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'tu_clave_secreta_aqui')

# Configuración de la base de datos
DATABASE = os.environ.get('DATABASE_URL', 'canto_gregoriano.db')

def init_db():
    """Inicializa la base de datos con las tablas necesarias"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Tabla para artículos del blog
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT NOT NULL,
            fecha_publicacion DATETIME DEFAULT CURRENT_TIMESTAMP,
            autor TEXT DEFAULT 'Administrador',
            categoria TEXT DEFAULT 'General'
        )
    ''')
    
    # Tabla para eventos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            fecha_evento DATETIME,
            lugar TEXT,
            tipo_evento TEXT,
            fecha_publicacion DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabla para recursos multimedia
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            tipo TEXT NOT NULL, -- 'audio', 'video', 'partitura'
            archivo_path TEXT,
            url_externa TEXT,
            epoca TEXT,
            tipo_canto TEXT,
            comunidad_monastica TEXT,
            fecha_agregado DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabla para mensajes de contacto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensajes_contacto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            mensaje TEXT NOT NULL,
            fecha_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
            leido BOOLEAN DEFAULT FALSE
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Obtiene una conexión a la base de datos"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Rutas principales
@app.route('/')
def inicio():
    """Página de inicio"""
    conn = get_db_connection()
    # Obtener los últimos artículos y eventos
    articulos_recientes = conn.execute(
        'SELECT * FROM articulos ORDER BY fecha_publicacion DESC LIMIT 3'
    ).fetchall()
    
    eventos_proximos = conn.execute(
        'SELECT * FROM eventos WHERE fecha_evento >= date("now") ORDER BY fecha_evento ASC LIMIT 3'
    ).fetchall()
    
    conn.close()
    return render_template('inicio.html', 
                         articulos=articulos_recientes, 
                         eventos=eventos_proximos)

@app.route('/historia')
def historia():
    """Página de historia del canto gregoriano"""
    return render_template('historia.html')

@app.route('/biblioteca')
def biblioteca():
    """Página de biblioteca con recursos multimedia"""
    conn = get_db_connection()
    
    # Obtener filtros disponibles
    epocas = conn.execute('SELECT DISTINCT epoca FROM recursos WHERE epoca IS NOT NULL').fetchall()
    tipos_canto = conn.execute('SELECT DISTINCT tipo_canto FROM recursos WHERE tipo_canto IS NOT NULL').fetchall()
    comunidades = conn.execute('SELECT DISTINCT comunidad_monastica FROM recursos WHERE comunidad_monastica IS NOT NULL').fetchall()
    
    # Obtener recursos con filtros
    tipo_filtro = request.args.get('tipo', 'todos')
    epoca_filtro = request.args.get('epoca', 'todas')
    canto_filtro = request.args.get('canto', 'todos')
    comunidad_filtro = request.args.get('comunidad', 'todas')
    
    query = 'SELECT * FROM recursos WHERE 1=1'
    params = []
    
    if tipo_filtro != 'todos':
        query += ' AND tipo = ?'
        params.append(tipo_filtro)
    
    if epoca_filtro != 'todas':
        query += ' AND epoca = ?'
        params.append(epoca_filtro)
    
    if canto_filtro != 'todos':
        query += ' AND tipo_canto = ?'
        params.append(canto_filtro)
    
    if comunidad_filtro != 'todas':
        query += ' AND comunidad_monastica = ?'
        params.append(comunidad_filtro)
    
    query += ' ORDER BY fecha_agregado DESC'
    
    recursos = conn.execute(query, params).fetchall()
    conn.close()
    
    return render_template('biblioteca.html', 
                         recursos=recursos,
                         epocas=epocas,
                         tipos_canto=tipos_canto,
                         comunidades=comunidades,
                         filtros_actuales={
                             'tipo': tipo_filtro,
                             'epoca': epoca_filtro,
                             'canto': canto_filtro,
                             'comunidad': comunidad_filtro
                         })

@app.route('/blog')
def blog():
    """Página del blog con artículos"""
    conn = get_db_connection()
    articulos = conn.execute(
        'SELECT * FROM articulos ORDER BY fecha_publicacion DESC'
    ).fetchall()
    conn.close()
    return render_template('blog.html', articulos=articulos)

@app.route('/blog/<int:articulo_id>')
def ver_articulo(articulo_id):
    """Ver un artículo específico"""
    conn = get_db_connection()
    articulo = conn.execute(
        'SELECT * FROM articulos WHERE id = ?', (articulo_id,)
    ).fetchone()
    conn.close()
    
    if articulo is None:
        flash('Artículo no encontrado', 'error')
        return redirect(url_for('blog'))
    
    return render_template('ver_articulo.html', articulo=articulo)

@app.route('/eventos')
def eventos():
    """Página de eventos"""
    conn = get_db_connection()
    eventos = conn.execute(
        'SELECT * FROM eventos ORDER BY fecha_evento ASC'
    ).fetchall()
    conn.close()
    return render_template('eventos.html', eventos=eventos)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    """Página de contacto"""
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        
        if nombre and email and mensaje:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO mensajes_contacto (nombre, email, mensaje) VALUES (?, ?, ?)',
                (nombre, email, mensaje)
            )
            conn.commit()
            conn.close()
            flash('Mensaje enviado correctamente. Gracias por contactarnos.', 'success')
            return redirect(url_for('contacto'))
        else:
            flash('Por favor, completa todos los campos.', 'error')
    
    return render_template('contacto.html')

@app.route('/gregorio')
def gregorio():
    """Sección didáctica con generador de canto gregoriano"""
    return render_template('gregorio.html')

@app.route('/api/process-gabc', methods=['POST'])
def process_gabc():
    """Procesa archivo GABC y devuelve datos para el generador"""
    if 'gabc_file' not in request.files:
        return jsonify({'error': 'No se encontró archivo'}), 400
    
    file = request.files['gabc_file']
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó archivo'}), 400
    
    if file and file.filename.endswith('.gabc'):
        try:
            # Leer contenido del archivo
            content = file.read().decode('utf-8')
            
            # Procesar el archivo GABC
            processed_data = process_gabc_content(content)
            
            return jsonify({
                'success': True,
                'data': processed_data
            })
        except Exception as e:
            return jsonify({'error': f'Error procesando archivo: {str(e)}'}), 500
    
    return jsonify({'error': 'Formato de archivo no válido'}), 400

def process_gabc_content(content):
    """Procesa el contenido de un archivo GABC"""
    # Parser básico de GABC
    lines = content.strip().split('\n')
    processed_data = {
        'title': 'Canto Gregoriano',
        'mode': 'Dorian',
        'notes': [],
        'lyrics': '',
        'clef': 'c',
        'key': 'd',
        'raw_content': content
    }
    
    # Buscar metadatos en el header
    for line in lines:
        if line.startswith('name:'):
            processed_data['title'] = line.split(':', 1)[1].strip()
        elif line.startswith('mode:'):
            processed_data['mode'] = line.split(':', 1)[1].strip()
        elif line.startswith('clef:'):
            processed_data['clef'] = line.split(':', 1)[1].strip()
    
    # Buscar la línea de música (después de %%)
    music_line = None
    lyrics_line = None
    in_music_section = False
    
    for line in lines:
        if line.strip() == '%%':
            in_music_section = True
            continue
        elif in_music_section and line.strip():
            if not music_line:
                music_line = line.strip()
            elif not lyrics_line:
                lyrics_line = line.strip()
                break
    
    if music_line:
        # Parsear la línea de música GABC
        processed_data['notes'] = parse_gabc_music(music_line)
        processed_data['lyrics'] = lyrics_line or ''
    
    return processed_data

def parse_gabc_music(music_line):
    """Parsea una línea de música GABC en notas individuales"""
    notes = []
    i = 0
    
    while i < len(music_line):
        char = music_line[i]
        
        if char in 'abcdefghijklmnopqrstuvwxyz':
            # Nota básica
            note = {
                'pitch': char,
                'duration': 1,
                'text': '',
                'type': 'note',
                'modifiers': []
            }
            
            # Verificar modificadores
            j = i + 1
            while j < len(music_line):
                next_char = music_line[j]
                if next_char == "'":
                    note['pitch'] = char.upper()  # Octava superior
                    note['modifiers'].append('high')
                    j += 1
                elif next_char == ',':
                    note['pitch'] = char.lower()  # Octava inferior
                    note['modifiers'].append('low')
                    j += 1
                elif next_char in '0123456789':
                    # Duración numérica
                    duration_str = ''
                    while j < len(music_line) and music_line[j] in '0123456789':
                        duration_str += music_line[j]
                        j += 1
                    note['duration'] = int(duration_str) if duration_str else 1
                    j -= 1
                elif next_char in '()':
                    # Agrupación de notas
                    if next_char == '(':
                        note['modifiers'].append('group_start')
                    else:
                        note['modifiers'].append('group_end')
                    j += 1
                else:
                    break
            
            notes.append(note)
            i = j
        
        elif char in '()':
            # Agrupación
            note = {
                'pitch': '',
                'duration': 1,
                'text': '',
                'type': 'group',
                'group_type': 'open' if char == '(' else 'close'
            }
            notes.append(note)
        
        elif char in '.,;:':
            # Pausas
            duration_map = {'.': 1, ',': 2, ';': 3, ':': 4}
            note = {
                'pitch': '',
                'duration': duration_map.get(char, 1),
                'text': '',
                'type': 'rest'
            }
            notes.append(note)
        
        elif char in '0123456789':
            # Duración standalone
            duration_str = ''
            while i < len(music_line) and music_line[i] in '0123456789':
                duration_str += music_line[i]
                i += 1
            # Esta duración se aplicará a la siguiente nota
            if notes:
                notes[-1]['duration'] = int(duration_str)
            i -= 1
        
        elif char == ' ':
            # Espacio - puede indicar separación de sílabas
            if notes:
                notes[-1]['text'] += ' '
        
        else:
            # Caracteres especiales o texto
            if char.isalpha():
                # Texto de la letra
                if notes:
                    notes[-1]['text'] += char
        
        i += 1
    
    return notes

# API endpoints para AJAX
@app.route('/api/recursos')
def api_recursos():
    """API para obtener recursos con filtros"""
    conn = get_db_connection()
    
    tipo_filtro = request.args.get('tipo', 'todos')
    epoca_filtro = request.args.get('epoca', 'todas')
    canto_filtro = request.args.get('canto', 'todos')
    comunidad_filtro = request.args.get('comunidad', 'todas')
    
    query = 'SELECT * FROM recursos WHERE 1=1'
    params = []
    
    if tipo_filtro != 'todos':
        query += ' AND tipo = ?'
        params.append(tipo_filtro)
    
    if epoca_filtro != 'todas':
        query += ' AND epoca = ?'
        params.append(epoca_filtro)
    
    if canto_filtro != 'todos':
        query += ' AND tipo_canto = ?'
        params.append(canto_filtro)
    
    if comunidad_filtro != 'todas':
        query += ' AND comunidad_monastica = ?'
        params.append(comunidad_filtro)
    
    query += ' ORDER BY fecha_agregado DESC'
    
    recursos = conn.execute(query, params).fetchall()
    conn.close()
    
    return jsonify([dict(recurso) for recurso in recursos])

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
