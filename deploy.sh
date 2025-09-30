#!/bin/bash

# Script de despliegue para VPS
echo "🚀 Iniciando despliegue del proyecto de Canto Gregoriano..."

# Actualizar sistema
echo "📦 Actualizando sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar Python y dependencias
echo "🐍 Instalando Python y dependencias..."
sudo apt install python3 python3-pip python3-venv nginx supervisor -y

# Crear directorio del proyecto
echo "📁 Creando directorio del proyecto..."
sudo mkdir -p /var/www/cantogregoriano
sudo chown -R $USER:$USER /var/www/cantogregoriano

# Clonar repositorio (reemplaza con tu URL)
echo "📥 Clonando repositorio..."
cd /var/www/cantogregoriano
# git clone https://github.com/tu-usuario/asce_proto.git .

# Crear entorno virtual
echo "🔧 Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
echo "📚 Instalando dependencias Python..."
pip install -r requirements.txt

# Configurar base de datos
echo "🗄️ Inicializando base de datos..."
python3 init_db.py
python3 sample_data.py

# Configurar Nginx
echo "🌐 Configurando Nginx..."
sudo tee /etc/nginx/sites-available/cantogregoriano << EOF
server {
    listen 80;
    server_name tu-dominio.com www.tu-dominio.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }

    location /static {
        alias /var/www/cantogregoriano/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
EOF

# Habilitar sitio
sudo ln -s /etc/nginx/sites-available/cantogregoriano /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Configurar Supervisor
echo "👨‍💼 Configurando Supervisor..."
sudo tee /etc/supervisor/conf.d/cantogregoriano.conf << EOF
[program:cantogregoriano]
command=/var/www/cantogregoriano/venv/bin/python app_production.py
directory=/var/www/cantogregoriano
user=www-data
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/cantogregoriano.log
environment=PATH="/var/www/cantogregoriano/venv/bin"
EOF

# Reiniciar Supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start cantogregoriano

echo "✅ ¡Despliegue completado!"
echo "🌐 Tu aplicación estará disponible en: http://tu-dominio.com"
echo "📊 Para monitorear: sudo supervisorctl status cantogregoriano"
echo "📝 Logs: tail -f /var/log/cantogregoriano.log"
