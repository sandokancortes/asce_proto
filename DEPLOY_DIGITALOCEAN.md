# 🚀 Guía de Despliegue en DigitalOcean

## 📋 Requisitos Previos

### 1. **Cuenta en DigitalOcean**
- Ve a [digitalocean.com](https://digitalocean.com)
- Regístrate con tu email
- **Necesitas una tarjeta de crédito** para verificación (no se cobra nada inicialmente)

### 2. **Cuenta en GitHub (Recomendado)**
- Ve a [github.com](https://github.com)
- Crea una cuenta gratuita
- Sube tu proyecto a un repositorio

### 3. **Cliente SSH (Windows)**
- **Git Bash** (viene con Git)
- **PuTTY** (alternativa)
- **Windows Terminal** (recomendado)

## 🖥️ Paso 1: Crear Droplet en DigitalOcean

### 1.1 Acceder a DigitalOcean
1. Inicia sesión en tu cuenta
2. Click en **"Create"** → **"Droplets"**

### 1.2 Configurar el Droplet
```
Imagen: Ubuntu 22.04 (LTS) x64
Plan: Basic
- $4/mes: 1GB RAM, 1 CPU, 25GB SSD
- $6/mes: 1GB RAM, 1 CPU, 25GB SSD + 1TB transferencia

Región: 
- Nueva York (más barato)
- San Francisco (más rápido para México)

Autenticación:
- SSH Key (recomendado)
- Password (más simple)
```

### 1.3 Configurar SSH Key (Recomendado)
```bash
# En tu computadora Windows (Git Bash)
ssh-keygen -t rsa -b 4096 -C "tu-email@ejemplo.com"
# Presiona Enter para usar ubicación por defecto
# Presiona Enter para no usar passphrase

# Copiar la clave pública
cat ~/.ssh/id_rsa.pub
```

1. En DigitalOcean, click **"New SSH Key"**
2. Pega el contenido de `id_rsa.pub`
3. Dale un nombre como "Mi Laptop"

### 1.4 Crear el Droplet
1. Dale un nombre: `cantogregoriano-server`
2. Click **"Create Droplet"**
3. Espera 1-2 minutos a que se cree

## 🔑 Paso 2: Conectar al Servidor

### 2.1 Obtener IP del Servidor
1. En DigitalOcean, ve a **"Droplets"**
2. Copia la **IP Address** de tu servidor

### 2.2 Conectar por SSH
```bash
# Conectar al servidor
ssh root@TU-IP-DEL-SERVIDOR

# Si usaste password, te pedirá la contraseña
# Si usaste SSH key, debería conectarse automáticamente
```

## 📦 Paso 3: Preparar el Servidor

### 3.1 Actualizar el Sistema
```bash
# Actualizar paquetes
apt update && apt upgrade -y

# Instalar dependencias básicas
apt install -y python3 python3-pip python3-venv nginx supervisor git
```

### 3.2 Crear Usuario para la Aplicación
```bash
# Crear usuario
adduser --system --group --shell /bin/bash cantogregoriano

# Crear directorio del proyecto
mkdir -p /var/www/cantogregoriano
chown cantogregoriano:cantogregoriano /var/www/cantogregoriano
```

## 📁 Paso 4: Subir el Proyecto

### Opción A: Desde GitHub (Recomendado)
```bash
# Cambiar al usuario de la aplicación
su - cantogregoriano
cd /var/www/cantogregoriano

# Clonar tu repositorio
git clone https://github.com/TU-USUARIO/asce_proto.git .

# O si es privado, usar token
git clone https://TU-TOKEN@github.com/TU-USUARIO/asce_proto.git .
```

### Opción B: Subir Archivos Manualmente
```bash
# En tu computadora (Git Bash)
scp -r . root@TU-IP:/var/www/cantogregoriano/
```

## 🐍 Paso 5: Configurar Python

### 5.1 Crear Entorno Virtual
```bash
# Como usuario cantogregoriano
cd /var/www/cantogregoriano
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 5.2 Configurar Base de Datos
```bash
# Inicializar base de datos
python3 init_db.py
python3 sample_data.py
```

## 🌐 Paso 6: Configurar Nginx

### 6.1 Crear Configuración de Nginx
```bash
# Como root
nano /etc/nginx/sites-available/cantogregoriano
```

### 6.2 Contenido del Archivo
```nginx
server {
    listen 80;
    server_name TU-DOMINIO.com www.TU-DOMINIO.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /var/www/cantogregoriano/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

### 6.3 Habilitar el Sitio
```bash
# Habilitar sitio
ln -s /etc/nginx/sites-available/cantogregoriano /etc/nginx/sites-enabled/

# Eliminar sitio por defecto
rm /etc/nginx/sites-enabled/default

# Probar configuración
nginx -t

# Reiniciar Nginx
systemctl restart nginx
systemctl enable nginx
```

## 👨‍💼 Paso 7: Configurar Supervisor

### 7.1 Crear Configuración de Supervisor
```bash
# Como root
nano /etc/supervisor/conf.d/cantogregoriano.conf
```

### 7.2 Contenido del Archivo
```ini
[program:cantogregoriano]
command=/var/www/cantogregoriano/venv/bin/python app_production.py
directory=/var/www/cantogregoriano
user=cantogregoriano
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/cantogregoriano.log
environment=PATH="/var/www/cantogregoriano/venv/bin"
```

### 7.3 Iniciar la Aplicación
```bash
# Recargar configuración
supervisorctl reread
supervisorctl update

# Iniciar aplicación
supervisorctl start cantogregoriano

# Verificar estado
supervisorctl status cantogregoriano
```

## 🔒 Paso 8: Configurar SSL (Opcional pero Recomendado)

### 8.1 Instalar Certbot
```bash
apt install -y certbot python3-certbot-nginx
```

### 8.2 Obtener Certificado SSL
```bash
# Reemplaza TU-DOMINIO.com con tu dominio real
certbot --nginx -d TU-DOMINIO.com -d www.TU-DOMINIO.com
```

## ✅ Paso 9: Verificar Despliegue

### 9.1 Verificar que Todo Funciona
```bash
# Verificar Nginx
systemctl status nginx

# Verificar aplicación
supervisorctl status cantogregoriano

# Ver logs
tail -f /var/log/cantogregoriano.log

# Verificar puerto
netstat -tlnp | grep :5000
```

### 9.2 Acceder a la Aplicación
- **Sin dominio:** `http://TU-IP-DEL-SERVIDOR`
- **Con dominio:** `http://TU-DOMINIO.com`

## 🛠️ Comandos Útiles para Mantenimiento

### Reiniciar Aplicación
```bash
supervisorctl restart cantogregoriano
```

### Ver Logs
```bash
tail -f /var/log/cantogregoriano.log
```

### Actualizar Código
```bash
# Como usuario cantogregoriano
cd /var/www/cantogregoriano
git pull origin main
supervisorctl restart cantogregoriano
```

### Backup de Base de Datos
```bash
cp /var/www/cantogregoriano/canto_gregoriano.db /var/www/cantogregoriano/backup_$(date +%Y%m%d).db
```

## 💰 Costos Estimados

- **Droplet DigitalOcean:** $4-6/mes
- **Dominio (opcional):** $10-15/año
- **Total:** ~$5/mes

## 🆘 Solución de Problemas

### Error: "Permission denied"
```bash
chown -R cantogregoriano:cantogregoriano /var/www/cantogregoriano
```

### Error: "Port 5000 already in use"
```bash
# Encontrar proceso
lsof -i :5000
# Matar proceso
kill -9 PID_DEL_PROCESO
```

### Error: "Module not found"
```bash
# Activar entorno virtual
source /var/www/cantogregoriano/venv/bin/activate
pip install -r requirements.txt
```

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs: `tail -f /var/log/cantogregoriano.log`
2. Verifica el estado: `supervisorctl status cantogregoriano`
3. Revisa Nginx: `systemctl status nginx`
