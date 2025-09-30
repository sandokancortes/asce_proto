#!/usr/bin/env python3
"""
Script para poblar la base de datos con datos de ejemplo
Ejecutar después de crear la base de datos inicial
"""

import sqlite3
from datetime import datetime, timedelta

def init_sample_data():
    """Poblar la base de datos con datos de ejemplo"""
    conn = sqlite3.connect('canto_gregoriano.db')
    cursor = conn.cursor()
    
    # Limpiar datos existentes
    cursor.execute('DELETE FROM articulos')
    cursor.execute('DELETE FROM eventos')
    cursor.execute('DELETE FROM recursos')
    cursor.execute('DELETE FROM mensajes_contacto')
    
    # Insertar artículos de ejemplo
    articulos_ejemplo = [
        {
            'titulo': 'Los Orígenes del Canto Gregoriano: Una Tradición Milenaria',
            'contenido': '''El canto gregoriano, también conocido como canto llano, representa una de las tradiciones musicales más antiguas y venerables de la humanidad. Sus raíces se remontan a los primeros siglos del cristianismo, cuando las comunidades cristianas comenzaron a desarrollar formas musicales para acompañar sus celebraciones litúrgicas.

La tradición atribuye al Papa Gregorio I (590-604) la organización y codificación de este repertorio musical, aunque en realidad el proceso fue mucho más complejo y gradual. El canto gregoriano no fue creado por un solo hombre, sino que evolucionó durante siglos, incorporando elementos de diversas tradiciones musicales del Mediterráneo.

Durante los siglos VII y VIII, se produjo una unificación gradual de las tradiciones musicales regionales, dando lugar al canto gregoriano tal como lo conocemos hoy. Esta unificación fue impulsada por la reforma carolingia y el deseo de estandarizar las prácticas litúrgicas en todo el imperio.

El canto gregoriano se caracteriza por su monodia (una sola línea melódica), su modalidad (uso de los ocho modos eclesiásticos) y su notación neumática, que permitió la preservación y transmisión de este repertorio a través de los siglos.''',
            'autor': 'Dr. María González',
            'categoria': 'Historia'
        },
        {
            'titulo': 'La Importancia de la Respiración en el Canto Gregoriano',
            'contenido': '''La respiración es fundamental en la interpretación del canto gregoriano. A diferencia de otros estilos vocales, el canto gregoriano requiere un control respiratorio específico que permite mantener la línea melódica sin interrupciones bruscas.

La técnica respiratoria en el canto gregoriano se basa en la respiración diafragmática, que permite un mayor control del aire y una emisión más estable del sonido. Esta técnica es especialmente importante en los cantos más largos, donde es necesario mantener la continuidad melódica.

Los cantores deben aprender a respirar de manera que no interrumpa el flujo musical. Esto implica respirar en puntos estratégicos de la melodía, generalmente al final de las frases musicales, y hacerlo de manera que sea prácticamente imperceptible para el oyente.

La respiración también está íntimamente relacionada con la interpretación del texto. En el canto gregoriano, la música está al servicio de la palabra, y la respiración debe respetar la estructura del texto latino, respirando en las pausas naturales del discurso.''',
            'autor': 'Prof. Juan Martínez',
            'categoria': 'Técnica'
        },
        {
            'titulo': 'Los Modos Eclesiásticos: Una Guía Completa',
            'contenido': '''Los ocho modos eclesiásticos constituyen el sistema modal del canto gregoriano. Cada modo tiene sus propias características melódicas y expresivas, y su comprensión es esencial para una interpretación auténtica del repertorio.

Los modos se dividen en dos grupos principales: los modos auténticos (I, II, III, IV) y los modos plagales (V, VI, VII, VIII). Los modos plagales tienen un rango más bajo que sus correspondientes auténticos, pero comparten la misma finalis (nota final).

Modo I (Dórico): Caracterizado por su solemnidad y gravedad, es ideal para textos de carácter penitencial o de lamento.

Modo II (Hipodórico): Similar al modo I pero con un rango más bajo, se utiliza frecuentemente en antífonas y responsorios.

Modo III (Frigio): Conocido por su carácter expresivo y emotivo, es especialmente adecuado para textos que expresan dolor o súplica.

Modo IV (Hipofrigio): Versión plagal del modo III, mantiene su carácter expresivo pero con un rango más grave.

Modo V (Lidio): De carácter brillante y alegre, se utiliza en textos de alabanza y acción de gracias.

Modo VI (Hipolidio): Versión plagal del modo V, conserva su carácter alegre pero con mayor profundidad.

Modo VII (Mixolidio): Caracterizado por su nobleza y dignidad, es frecuente en himnos y cantos de carácter festivo.

Modo VIII (Hipomixolidio): Versión plagal del modo VII, mantiene su nobleza pero con un carácter más íntimo.''',
            'autor': 'Dr. Ana Rodríguez',
            'categoria': 'Teoría Musical'
        },
        {
            'titulo': 'El Canto Gregoriano en la Liturgia Moderna',
            'contenido': '''A pesar de los cambios litúrgicos introducidos por el Concilio Vaticano II, el canto gregoriano mantiene su lugar privilegiado en la liturgia católica. El documento Sacrosanctum Concilium reconoce explícitamente el valor del canto gregoriano como "canto propio de la liturgia romana".

En la liturgia moderna, el canto gregoriano puede coexistir con otras formas musicales, enriqueciendo la celebración litúrgica. Su uso no se limita a las misas en latín, sino que puede adaptarse a las celebraciones en lengua vernácula.

Los cantos gregorianos más utilizados en la liturgia actual incluyen el Kyrie, el Gloria, el Sanctus y el Agnus Dei, así como las antífonas del salmo responsorial y los cantos de entrada y comunión.

La interpretación del canto gregoriano en la liturgia moderna requiere un equilibrio entre la fidelidad a la tradición y la adaptación a las necesidades actuales. Esto implica respetar las características esenciales del canto mientras se asegura que sea comprensible y significativo para la asamblea.''',
            'autor': 'P. Miguel Santos',
            'categoria': 'Liturgia'
        },
        {
            'titulo': 'Comunidades Monásticas: Guardianes de la Tradición',
            'contenido': '''Las comunidades monásticas han sido durante siglos los principales guardianes y transmisores del canto gregoriano. Desde la Edad Media, los monasterios han mantenido viva esta tradición musical, preservándola a través de la enseñanza oral y la copia de manuscritos.

La abadía de Solesmes, en Francia, ha jugado un papel especialmente importante en la restauración y difusión del canto gregoriano en los siglos XIX y XX. Los monjes de Solesmes, bajo la dirección de Dom Guéranger y sus sucesores, dedicaron décadas al estudio de los manuscritos medievales para reconstruir la interpretación auténtica del canto gregoriano.

Otras comunidades monásticas importantes en la preservación del canto gregoriano incluyen la abadía de Santo Domingo de Silos en España, la abadía de Heiligenkreuz en Austria, y la abadía de Clear Creek en Estados Unidos.

El estilo de vida monástico, con su énfasis en la oración, el silencio y la contemplación, proporciona el contexto ideal para la interpretación del canto gregoriano. Los monjes no solo preservan la tradición musical, sino que la viven como parte integral de su vida espiritual.''',
            'autor': 'Dom Carlos Mendoza',
            'categoria': 'Comunidad'
        }
    ]
    
    for articulo in articulos_ejemplo:
        cursor.execute('''
            INSERT INTO articulos (titulo, contenido, autor, categoria, fecha_publicacion)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            articulo['titulo'],
            articulo['contenido'],
            articulo['autor'],
            articulo['categoria'],
            datetime.now() - timedelta(days=len(articulos_ejemplo) - articulos_ejemplo.index(articulo))
        ))
    
    # Insertar eventos de ejemplo
    eventos_ejemplo = [
        {
            'titulo': 'Misa Dominical con Canto Gregoriano',
            'descripcion': 'Celebración de la misa dominical con canto gregoriano tradicional. Incluye Kyrie, Gloria, Sanctus y Agnus Dei en latín.',
            'fecha_evento': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S'),
            'lugar': 'Iglesia de San Francisco, Centro Histórico',
            'tipo_evento': 'misa'
        },
        {
            'titulo': 'Concierto de Canto Gregoriano: "Adventus Domini"',
            'descripcion': 'Concierto especial de Adviento con cantos gregorianos tradicionales del tiempo de preparación para la Navidad.',
            'fecha_evento': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d %H:%M:%S'),
            'lugar': 'Catedral Metropolitana',
            'tipo_evento': 'concierto'
        },
        {
            'titulo': 'Taller de Interpretación del Canto Gregoriano',
            'descripcion': 'Taller práctico para aprender las técnicas básicas de interpretación del canto gregoriano. Dirigido a principiantes.',
            'fecha_evento': (datetime.now() + timedelta(days=21)).strftime('%Y-%m-%d %H:%M:%S'),
            'lugar': 'Centro Cultural San Agustín',
            'tipo_evento': 'clase'
        },
        {
            'titulo': 'Conferencia: "El Canto Gregoriano en la Música Contemporánea"',
            'descripcion': 'Conferencia magistral sobre la influencia del canto gregoriano en compositores contemporáneos como Arvo Pärt y John Tavener.',
            'fecha_evento': (datetime.now() + timedelta(days=28)).strftime('%Y-%m-%d %H:%M:%S'),
            'lugar': 'Auditorio de la Universidad Católica',
            'tipo_evento': 'conferencia'
        }
    ]
    
    for evento in eventos_ejemplo:
        cursor.execute('''
            INSERT INTO eventos (titulo, descripcion, fecha_evento, lugar, tipo_evento, fecha_publicacion)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            evento['titulo'],
            evento['descripcion'],
            evento['fecha_evento'],
            evento['lugar'],
            evento['tipo_evento'],
            datetime.now()
        ))
    
    # Insertar recursos de ejemplo
    recursos_ejemplo = [
        {
            'titulo': 'Kyrie Eleison - Modo I',
            'descripcion': 'Grabación histórica del Kyrie en modo dórico, interpretado por el coro de la abadía de Solesmes.',
            'tipo': 'audio',
            'archivo_path': 'kyrie_eleison_modo1.mp3',
            'epoca': 'Medieval',
            'tipo_canto': 'Ordinario de la Misa',
            'comunidad_monastica': 'Abadía de Solesmes'
        },
        {
            'titulo': 'Salve Regina - Antífona Mariana',
            'descripcion': 'Interpretación de la antífona mariana Salve Regina en modo V (lidio).',
            'tipo': 'audio',
            'archivo_path': 'salve_regina.mp3',
            'epoca': 'Medieval',
            'tipo_canto': 'Antífona',
            'comunidad_monastica': 'Abadía de Santo Domingo de Silos'
        },
        {
            'titulo': 'Concierto de Canto Gregoriano - Abadía de Heiligenkreuz',
            'descripcion': 'Concierto completo de canto gregoriano interpretado por los monjes de la abadía de Heiligenkreuz, Austria.',
            'tipo': 'video',
            'url_externa': 'https://www.youtube.com/watch?v=ejemplo1',
            'epoca': 'Contemporánea',
            'tipo_canto': 'Concierto',
            'comunidad_monastica': 'Abadía de Heiligenkreuz'
        },
        {
            'titulo': 'Partitura: Gradual "Haec dies"',
            'descripcion': 'Partitura en notación cuadrada del gradual Haec dies para el domingo de Pascua.',
            'tipo': 'partitura',
            'archivo_path': 'haec_dies_gradual.pdf',
            'epoca': 'Medieval',
            'tipo_canto': 'Gradual',
            'comunidad_monastica': 'Tradición Romana'
        },
        {
            'titulo': 'Ave Maria - Modo VIII',
            'descripcion': 'Grabación de la antífona Ave Maria en modo hipomixolidio.',
            'tipo': 'audio',
            'archivo_path': 'ave_maria_modo8.mp3',
            'epoca': 'Medieval',
            'tipo_canto': 'Antífona',
            'comunidad_monastica': 'Abadía de Clear Creek'
        },
        {
            'titulo': 'Taller de Canto Gregoriano - Técnicas Básicas',
            'descripcion': 'Video tutorial sobre las técnicas básicas de interpretación del canto gregoriano.',
            'tipo': 'video',
            'url_externa': 'https://www.youtube.com/watch?v=ejemplo2',
            'epoca': 'Contemporánea',
            'tipo_canto': 'Educativo',
            'comunidad_monastica': 'Centro de Estudios Gregorianos'
        },
        {
            'titulo': 'Partitura: Introito "Resurrexi"',
            'descripcion': 'Partitura del introito Resurrexi para el domingo de Pascua en notación gregoriana.',
            'tipo': 'partitura',
            'archivo_path': 'resurrexi_introito.pdf',
            'epoca': 'Medieval',
            'tipo_canto': 'Introito',
            'comunidad_monastica': 'Tradición Romana'
        },
        {
            'titulo': 'Veni Creator Spiritus - Himno',
            'descripcion': 'Grabación del himno Veni Creator Spiritus, tradicionalmente cantado en Pentecostés.',
            'tipo': 'audio',
            'archivo_path': 'veni_creator_spiritus.mp3',
            'epoca': 'Medieval',
            'tipo_canto': 'Himno',
            'comunidad_monastica': 'Abadía de Solesmes'
        }
    ]
    
    for recurso in recursos_ejemplo:
        cursor.execute('''
            INSERT INTO recursos (titulo, descripcion, tipo, archivo_path, url_externa, epoca, tipo_canto, comunidad_monastica, fecha_agregado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            recurso['titulo'],
            recurso['descripcion'],
            recurso['tipo'],
            recurso.get('archivo_path'),
            recurso.get('url_externa'),
            recurso['epoca'],
            recurso['tipo_canto'],
            recurso['comunidad_monastica'],
            datetime.now()
        ))
    
    # Insertar mensajes de contacto de ejemplo
    mensajes_ejemplo = [
        {
            'nombre': 'Carlos Mendoza',
            'email': 'carlos.mendoza@email.com',
            'mensaje': 'Me interesa mucho aprender canto gregoriano. ¿Ofrecen clases para principiantes?',
            'fecha_envio': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'nombre': 'Ana García',
            'email': 'ana.garcia@email.com',
            'mensaje': 'Tengo algunas grabaciones históricas de canto gregoriano que me gustaría compartir con la comunidad.',
            'fecha_envio': (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'nombre': 'Miguel Santos',
            'email': 'miguel.santos@email.com',
            'mensaje': '¿Podrían organizar un concierto de canto gregoriano en nuestra parroquia?',
            'fecha_envio': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        }
    ]
    
    for mensaje in mensajes_ejemplo:
        cursor.execute('''
            INSERT INTO mensajes_contacto (nombre, email, mensaje, fecha_envio)
            VALUES (?, ?, ?, ?)
        ''', (
            mensaje['nombre'],
            mensaje['email'],
            mensaje['mensaje'],
            mensaje['fecha_envio']
        ))
    
    conn.commit()
    conn.close()
    
    print("Datos de ejemplo insertados correctamente:")
    print(f"   - {len(articulos_ejemplo)} articulos")
    print(f"   - {len(eventos_ejemplo)} eventos")
    print(f"   - {len(recursos_ejemplo)} recursos")
    print(f"   - {len(mensajes_ejemplo)} mensajes de contacto")

if __name__ == '__main__':
    init_sample_data()
