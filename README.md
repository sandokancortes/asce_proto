# Sitio Web de Canto Gregoriano

Un sitio web moderno y responsivo para difundir el canto gregoriano y crear comunidad en torno a esta tradición musical milenaria.

## Características

- **Diseño Moderno**: Interfaz limpia y elegante con tipografía serif para el contenido y sans-serif para la navegación
- **Totalmente Responsivo**: Optimizado para dispositivos móviles, tablets y escritorio
- **Biblioteca Multimedia**: Reproductor de audio integrado, visualizador de videos y descarga de partituras
- **Sistema de Filtros**: Búsqueda avanzada por época, tipo de canto y comunidad monástica
- **Blog Integrado**: Sistema de artículos con categorías y metadatos
- **Gestión de Eventos**: Calendario de eventos y sistema de registro
- **Formulario de Contacto**: Sistema de mensajes con validación en tiempo real

## Tecnologías Utilizadas

- **Backend**: Python Flask
- **Base de Datos**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript (jQuery)
- **Tipografía**: Google Fonts (Crimson Text, Open Sans)
- **Iconos**: Font Awesome
- **Diseño**: CSS Grid, Flexbox, CSS Variables

## Estructura del Proyecto

```
asce_proto/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias de Python
├── README.md             # Documentación del proyecto
├── templates/            # Templates HTML5
│   ├── base.html         # Template base
│   ├── inicio.html       # Página de inicio
│   ├── historia.html     # Página de historia
│   ├── biblioteca.html   # Biblioteca de recursos
│   ├── blog.html         # Blog y artículos
│   ├── ver_articulo.html # Vista individual de artículo
│   ├── eventos.html      # Página de eventos
│   └── contacto.html     # Formulario de contacto
└── static/               # Archivos estáticos
    ├── css/
    │   ├── style.css     # Estilos principales
    │   └── responsive.css # Estilos responsivos
    ├── js/
    │   └── main.js       # JavaScript principal
    ├── images/           # Imágenes del sitio
    ├── audio/            # Archivos de audio
    ├── videos/           # Archivos de video
    └── partituras/       # Archivos de partituras
```

## Instalación y Configuración

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd asce_proto
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

## Funcionalidades Principales

### 1. Página de Inicio
- Mensaje de bienvenida y misión del proyecto
- Enlaces rápidos a las secciones principales
- Artículos y eventos recientes
- Llamada a la acción para unirse a la comunidad

### 2. Historia del Canto Gregoriano
- Orígenes y evolución histórica
- Influencia en la música sacra y clásica
- Línea de tiempo interactiva
- Artículos especializados

### 3. Biblioteca de Recursos
- **Audios**: Reproductor integrado con controles personalizados
- **Videos**: Visualizador de videos embebidos
- **Partituras**: Descarga de archivos PDF
- **Filtros**: Por época, tipo de canto, comunidad monástica
- **Búsqueda**: Sistema de búsqueda en tiempo real

### 4. Blog y Artículos
- Sistema de artículos con categorías
- Metadatos (autor, fecha, categoría)
- Vista individual de artículos
- Artículos relacionados
- Funcionalidad de impresión

### 5. Eventos
- Calendario de eventos
- Filtros por tipo de evento
- Detalles de eventos
- Sistema de propuesta de eventos

### 6. Contacto
- Formulario de contacto con validación
- Información de contacto (email, teléfono, WhatsApp)
- Enlaces a redes sociales
- Preguntas frecuentes (FAQ)
- Centro de ayuda

## Base de Datos

El sitio utiliza SQLite con las siguientes tablas:

- **articulos**: Artículos del blog
- **eventos**: Eventos y celebraciones
- **recursos**: Recursos multimedia (audio, video, partituras)
- **mensajes_contacto**: Mensajes del formulario de contacto

## Personalización

### Colores
Los colores se definen en CSS variables en `static/css/style.css`:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #34495e;
    --accent-color: #e74c3c;
    --gold-color: #f39c12;
    /* ... más variables */
}
```

### Tipografía
- **Títulos**: Crimson Text (serif)
- **Texto**: Open Sans (sans-serif)

### Responsive Design
- **Mobile First**: Diseño optimizado para móviles
- **Breakpoints**: 576px, 768px, 992px, 1200px
- **Grid System**: CSS Grid y Flexbox

## Características de Accesibilidad

- Navegación por teclado
- Etiquetas semánticas HTML5
- Contraste de colores optimizado
- Soporte para lectores de pantalla
- Enlaces de salto para navegación rápida
- Modo de alto contraste
- Reducción de movimiento para usuarios sensibles

## Rendimiento

- Lazy loading de imágenes
- Compresión de archivos estáticos
- Optimización de CSS y JavaScript
- Monitoreo de Core Web Vitals
- Caché de navegador optimizado

## Seguridad

- Validación de formularios en frontend y backend
- Sanitización de entrada de usuario
- Protección CSRF (Cross-Site Request Forgery)
- Headers de seguridad HTTP

## Contribución

Para contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Para preguntas o sugerencias sobre el proyecto:
- Email: info@cantogregoriano.org
- WhatsApp: +1 (555) 123-4567

## Roadmap

### Próximas Funcionalidades
- [ ] Sistema de usuarios y autenticación
- [ ] Panel de administración
- [ ] Sistema de comentarios
- [ ] Integración con redes sociales
- [ ] API REST para aplicaciones móviles
- [ ] Sistema de donaciones
- [ ] Traducción a múltiples idiomas
- [ ] Integración con servicios de streaming
- [ ] Sistema de notificaciones push
- [ ] Analytics y métricas de uso

### Mejoras Técnicas
- [ ] Migración a PostgreSQL
- [ ] Implementación de Redis para caché
- [ ] Dockerización del proyecto
- [ ] CI/CD con GitHub Actions
- [ ] Tests automatizados
- [ ] Documentación API
- [ ] Monitoreo y logging avanzado
