# Dockerfile para Portafolio Reflex - Despliegue Estático
FROM python:3.12-slim as builder

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para Reflex
RUN apt-get update && apt-get install -y \
    curl \
    nodejs \
    npm \
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

# Inicializar Reflex y exportar sin SSR
RUN uv run reflex init && \
    uv run reflex export --frontend-only --no-ssr --no-zip

# Imagen final ligera solo con archivos estáticos
FROM nginx:alpine

# Copiar archivos estáticos al directorio de nginx
COPY --from=builder /app/.web/build/client /usr/share/nginx/html

# Configuración de nginx para SPA
RUN echo 'server { \
    listen 80; \
    server_name _; \
    root /usr/share/nginx/html; \
    index index.html; \
    location / { \
        try_files $uri $uri/ /index.html =404; \
        add_header Cache-Control "no-cache"; \
    } \
    location /assets/ { \
        expires 1y; \
        add_header Cache-Control "public, immutable"; \
    } \
}' > /etc/nginx/conf.d/default.conf

# Exponer el puerto
EXPOSE 80

# Nginx se ejecuta automáticamente
CMD ["nginx", "-g", "daemon off;"]
