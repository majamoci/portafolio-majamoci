# Dockerfile para Portafolio Reflex - Backend + Nginx Proxy
FROM python:3.12-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para Reflex + Nginx
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    nodejs \
    npm \
    nginx \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Actualizar npm
RUN npm install -g npm@latest

# Instalar uv para gestión rápida de paquetes
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copiar archivos de configuración del proyecto
COPY pyproject.toml .python-version ./

# Crear entorno virtual e instalar dependencias
RUN uv venv && uv pip install -r pyproject.toml

# Copiar todo el código de la aplicación
COPY . .

# Configurar Nginx (eliminar default, usar nuestro config)
RUN rm -f /etc/nginx/sites-enabled/default && \
    mkdir -p /var/www/html && \
    cp nginx.conf /etc/nginx/conf.d/default.conf

# Inicializar Reflex y exportar frontend estático
RUN uv run reflex init && \
    uv run reflex export --frontend-only --no-zip

# Copiar frontend compilado a Nginx
RUN cp -r .web/build/client/* /var/www/html/

# Script de inicio
RUN chmod +x /app/start.sh

# Solo exponemos puerto 80 (Nginx maneja todo)
EXPOSE 80

CMD ["/app/start.sh"]
