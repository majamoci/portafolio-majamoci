# Dockerfile para Portafolio Reflex - Dokploy
FROM python:3.11-slim

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

# Copiar archivos de requisitos
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código de la aplicación
COPY . .

# Inicializar Reflex (esto descarga las dependencias de Node y construye el frontend)
RUN reflex init

# Exportar la aplicación para producción (genera frontend.zip)
RUN reflex export --frontend-only

# Descomprimir archivos estáticos en public/
RUN unzip frontend.zip -d public && rm -f frontend.zip

# Exponer el puerto
EXPOSE 8000

# Variables de entorno para producción
ENV REFLEX_ENV=production

# Comando para servir los archivos estáticos desde public/
CMD ["python", "-m", "http.server", "8000", "--directory", "public"]
