# Dockerfile para Portafolio Reflex - Dokploy
FROM python:3.12-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para Reflex
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Actualizar npm a la última versión
RUN npm install -g npm@latest

# Instalar uv para gestión rápida de paquetes
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copiar archivos de configuración del proyecto
COPY pyproject.toml .
COPY .python-version .

# Crear entorno virtual e instalar dependencias
RUN uv venv && \
    uv pip install -r pyproject.toml

# Copiar todo el código de la aplicación
COPY . .

# Inicializar Reflex (esto descarga las dependencias de Node y construye el frontend)
RUN uv run reflex init

# Exportar la aplicación para producción (genera frontend.zip)
RUN uv run reflex export --frontend-only

# Descomprimir archivos estáticos en public/
RUN unzip frontend.zip -d public && rm -f frontend.zip

# Exponer el puerto
EXPOSE 8000

# Variables de entorno para producción
ENV REFLEX_ENV=production

# Comando para servir los archivos estáticos desde public/
CMD ["python", "-m", "http.server", "8000", "--directory", "public"]
