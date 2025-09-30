"""
Configuración de la aplicación Flask
"""

import os
from datetime import timedelta

class Config:
    """Configuración base"""
    
    # Configuración de la aplicación
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu-clave-secreta-muy-segura-aqui'
    
    # Configuración de la base de datos
    DATABASE = 'canto_gregoriano.db'
    
    # Configuración de archivos
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB máximo por archivo
    UPLOAD_FOLDER = 'static'
    ALLOWED_EXTENSIONS = {
        'audio': {'mp3', 'wav', 'ogg', 'm4a'},
        'video': {'mp4', 'avi', 'mov', 'wmv'},
        'partitura': {'pdf', 'jpg', 'jpeg', 'png'}
    }
    
    # Configuración de paginación
    ARTICLES_PER_PAGE = 10
    RESOURCES_PER_PAGE = 12
    EVENTS_PER_PAGE = 8
    
    # Configuración de sesión
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # Configuración de email (para futuras funcionalidades)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Configuración de redes sociales
    SOCIAL_MEDIA = {
        'facebook': 'https://facebook.com/cantogregoriano',
        'twitter': 'https://twitter.com/cantogregoriano',
        'youtube': 'https://youtube.com/cantogregoriano',
        'instagram': 'https://instagram.com/cantogregoriano'
    }
    
    # Configuración de contacto
    CONTACT_INFO = {
        'email': 'info@cantogregoriano.org',
        'phone': '+1 (555) 123-4567',
        'whatsapp': '+1 (555) 123-4567',
        'address': 'Centro Histórico, Ciudad'
    }
    
    # Configuración de SEO
    SITE_NAME = 'Canto Gregoriano'
    SITE_DESCRIPTION = 'Comunidad dedicada a preservar y difundir el canto gregoriano'
    SITE_KEYWORDS = 'canto gregoriano, música sacra, liturgia, tradición, monasterio'
    
    # Configuración de analytics (para futuras funcionalidades)
    GOOGLE_ANALYTICS_ID = os.environ.get('GOOGLE_ANALYTICS_ID')
    
    # Configuración de caché
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    TESTING = False
    
    # En producción, usar variables de entorno para datos sensibles
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Configuración de base de datos para producción
    DATABASE_URL = os.environ.get('DATABASE_URL')

class TestingConfig(Config):
    """Configuración para testing"""
    TESTING = True
    DATABASE = 'test_canto_gregoriano.db'
    WTF_CSRF_ENABLED = False

# Diccionario de configuraciones
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
