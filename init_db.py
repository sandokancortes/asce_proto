#!/usr/bin/env python3
"""
Script simple para inicializar la base de datos
"""

import sqlite3

def init_database():
    """Inicializa la base de datos con las tablas necesarias"""
    conn = sqlite3.connect('canto_gregoriano.db')
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
            tipo TEXT NOT NULL,
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
    print("Base de datos inicializada correctamente")

if __name__ == '__main__':
    init_database()
