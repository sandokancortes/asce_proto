# Guía de Instalación - Sitio Web de Canto Gregoriano

## Requisitos del Sistema

- **Python**: 3.7 o superior
- **Sistema Operativo**: Windows, macOS, o Linux
- **Navegador Web**: Chrome, Firefox, Safari, o Edge (versiones recientes)

## Instalación Paso a Paso

### 1. Preparar el Entorno

#### Opción A: Usar Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

#### Opción B: Instalación Global

Si prefieres instalar las dependencias globalmente (no recomendado):

```bash
# Asegúrate de tener pip actualizado
python -m pip install --upgrade pip
```

### 2. Instalar Dependencias

```bash
# Instalar todas las dependencias desde requirements.txt
pip install -r requirements.txt
```

### 3. Configurar la Base de Datos

```bash
# Ejecutar la aplicación por primera vez para crear la base de datos
python app.py
```

La aplicación creará automáticamente la base de datos SQLite `canto_gregoriano.db` con todas las tablas necesarias.

### 4. Poblar con Datos de Ejemplo (Opcional)

```bash
# Ejecutar el script de datos de ejemplo
python sample_data.py
```

Esto insertará artículos, eventos, recursos y mensajes de ejemplo en la base de datos.

### 5. Ejecutar la Aplicación

```bash
# Iniciar el servidor de desarrollo
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

## Estructura de Archivos Después de la Instalación

```
asce_proto/
├── app.py                    # ✅ Aplicación Flask principal
├── config.py                 # ✅ Configuración de la aplicación
├── sample_data.py            # ✅ Script de datos de ejemplo
├── requirements.txt          # ✅ Dependencias de Python
├── README.md                 # ✅ Documentación principal
├── INSTALACION.md            # ✅ Esta guía de instalación
├── canto_gregoriano.db       # 📁 Base de datos SQLite (se crea automáticamente)
├── templates/                # ✅ Templates HTML5
│   ├── base.html
│   ├── inicio.html
│   ├── historia.html
│   ├── biblioteca.html
│   ├── blog.html
│   ├── ver_articulo.html
│   ├── eventos.html
│   └── contacto.html
└── static/                   # ✅ Archivos estáticos
    ├── css/
    │   ├── style.css         # ✅ Estilos principales
    │   ├── responsive.css    # ✅ Estilos responsivos
    │   ├── audio-player.css  # ✅ Estilos del reproductor
    │   ├── forms.css         # ✅ Estilos de formularios
    │   └── components.css    # ✅ Estilos de componentes
    ├── js/
    │   └── main.js          # ✅ JavaScript principal
    ├── images/              # 📁 Imágenes (vacío, listo para usar)
    ├── audio/               # 📁 Archivos de audio (vacío, listo para usar)
    ├── videos/              # 📁 Archivos de video (vacío, listo para usar)
    └── partituras/          # 📁 Partituras (vacío, listo para usar)
```

## Verificación de la Instalación

### 1. Verificar que la Aplicación Funciona

1. Abre tu navegador web
2. Ve a `http://localhost:5000`
3. Deberías ver la página de inicio del sitio de Canto Gregoriano

### 2. Verificar las Funcionalidades

- ✅ **Navegación**: Prueba todos los enlaces del menú
- ✅ **Página de Inicio**: Verifica que se muestre correctamente
- ✅ **Historia**: Revisa la página de historia
- ✅ **Biblioteca**: Prueba los filtros y la visualización de recursos
- ✅ **Blog**: Verifica que se muestren los artículos
- ✅ **Eventos**: Revisa el calendario y la lista de eventos
- ✅ **Contacto**: Prueba el formulario de contacto

### 3. Verificar la Base de Datos

```bash
# Verificar que la base de datos se creó
ls -la canto_gregoriano.db

# Si ejecutaste sample_data.py, verificar que hay datos
python -c "
import sqlite3
conn = sqlite3.connect('canto_gregoriano.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM articulos')
print(f'Artículos: {cursor.fetchone()[0]}')
cursor.execute('SELECT COUNT(*) FROM eventos')
print(f'Eventos: {cursor.fetchone()[0]}')
cursor.execute('SELECT COUNT(*) FROM recursos')
print(f'Recursos: {cursor.fetchone()[0]}')
conn.close()
"
```

## Solución de Problemas Comunes

### Error: "ModuleNotFoundError: No module named 'flask'"

**Solución**: Instala Flask y las dependencias:
```bash
pip install -r requirements.txt
```

### Error: "Permission denied" al crear archivos

**Solución**: Verifica los permisos de escritura en el directorio:
```bash
# En Linux/macOS
chmod 755 .

# En Windows, ejecuta como administrador o cambia la ubicación del proyecto
```

### Error: "Address already in use"

**Solución**: El puerto 5000 está ocupado. Cambia el puerto:
```bash
# Modifica app.py línea final:
app.run(debug=True, port=5001)
```

### La página no carga o se ve mal

**Solución**: 
1. Verifica que todos los archivos CSS y JS estén en su lugar
2. Abre las herramientas de desarrollador del navegador (F12)
3. Revisa la consola para errores de JavaScript
4. Verifica que no hay errores 404 en la pestaña Network

### Los datos de ejemplo no aparecen

**Solución**:
```bash
# Ejecuta el script de datos de ejemplo
python sample_data.py

# Verifica que se ejecutó correctamente
# Deberías ver mensajes de confirmación
```

## Personalización Inicial

### 1. Cambiar la Información de Contacto

Edita `config.py`:
```python
CONTACT_INFO = {
    'email': 'tu-email@ejemplo.com',
    'phone': '+1 (555) 123-4567',
    'whatsapp': '+1 (555) 123-4567',
    'address': 'Tu Dirección, Ciudad'
}
```

### 2. Cambiar las Redes Sociales

Edita `config.py`:
```python
SOCIAL_MEDIA = {
    'facebook': 'https://facebook.com/tu-pagina',
    'twitter': 'https://twitter.com/tu-usuario',
    'youtube': 'https://youtube.com/tu-canal',
    'instagram': 'https://instagram.com/tu-usuario'
}
```

### 3. Agregar Contenido Personalizado

1. **Artículos**: Usa el formulario de contacto o edita directamente la base de datos
2. **Eventos**: Agrega eventos a través del formulario de contacto
3. **Recursos**: Coloca archivos en las carpetas `static/audio/`, `static/videos/`, `static/partituras/`

## Próximos Pasos

1. **Personalizar el Contenido**: Reemplaza los datos de ejemplo con tu contenido real
2. **Agregar Archivos Multimedia**: Sube grabaciones, videos y partituras
3. **Configurar Dominio**: Cuando estés listo, configura un dominio personalizado
4. **Backup**: Configura copias de seguridad regulares de la base de datos
5. **Monitoreo**: Implementa herramientas de monitoreo y analytics

## Soporte

Si encuentras problemas durante la instalación:

1. **Revisa esta guía** paso a paso
2. **Verifica los requisitos** del sistema
3. **Consulta los logs** de error en la consola
4. **Contacta al desarrollador** con detalles específicos del error

## Comandos Útiles

```bash
# Verificar versión de Python
python --version

# Verificar pip
pip --version

# Listar paquetes instalados
pip list

# Actualizar pip
python -m pip install --upgrade pip

# Desactivar entorno virtual
deactivate

# Ver logs de la aplicación
python app.py 2>&1 | tee app.log
```

¡Felicitaciones! Tu sitio web de Canto Gregoriano está listo para usar. 🎵
