#!/bin/bash

# Script de build para producción
# Requiere Python 3.12 y uv instalado

# Instalar uv si no está disponible
if ! command -v uv &> /dev/null; then
    echo "Instalando uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Crear entorno virtual y sincronizar dependencias
uv sync

# Limpiar directorio público anterior
rm -rf public

# Inicializar Reflex
uv run reflex init

# Exportar frontend para producción
uv run reflex export --frontend-only

# Descomprimir archivos estáticos
unzip frontend.zip -d public
rm -f frontend.zip

echo "Build completado exitosamente!"