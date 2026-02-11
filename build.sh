#!/bin/bash

# Script de build para producción estática
# Requiere Python 3.12 y uv instalado

set -e  # Salir si hay errores

echo "🚀 Iniciando build de producción..."

# Instalar uv si no está disponible
if ! command -v uv &> /dev/null; then
    echo "📦 Instalando uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Sincronizar dependencias
echo "📦 Instalando dependencias Python..."
uv sync

# Limpiar directorios anteriores
echo "🧹 Limpiando directorios anteriores..."
rm -rf public

# Inicializar Reflex
echo "⚙️  Inicializando Reflex..."
uv run reflex init

# Exportar sin SSR para sitio completamente estático
echo "🔨 Compilando sitio estático (sin SSR)..."
uv run reflex export --frontend-only --no-ssr --no-zip

# Copiar archivos del build al directorio public
echo "📂 Copiando archivos a public/..."
mkdir -p public

# Los archivos estáticos están en .web/build/client
if [ -d ".web/build/client" ]; then
    cp -r .web/build/client/* public/
fi

echo "✅ Build completado exitosamente!"
echo "📁 Archivos en: public/"
echo ""
echo "Para probar localmente:"
echo "  cd public && python3 -m http.server 8000"