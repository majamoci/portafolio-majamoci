# Dockerfile para Portafolio Reflex - Despliegue con Backend
FROM python:3.12-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para Reflex
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
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

# Inicializar Reflex (esto instala dependencias de Node y compila frontend)
RUN uv run reflex init

# Exponer puertos (3000 para frontend, 8000 para backend)
EXPOSE 3000 8000

# Variables de entorno para producción
ENV REFLEX_ENV=production
ENV REFLEX_BACKEND_ONLY=false

# Comando para ejecutar Reflex en modo producción
CMD ["uv", "run", "reflex", "run", "--env", "prod", "--backend-host", "0.0.0.0", "--backend-port", "8000", "--loglevel", "warning"]
