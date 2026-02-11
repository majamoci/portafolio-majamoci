#!/bin/bash

# Script de build y despliegue para Portafolio Reflex (con Backend)

set -e

echo "🚀 Construyendo imagen Docker del portafolio..."
echo ""

# Nombre de la imagen
IMAGE_NAME="portafolio-majamoci"
TAG="${1:-latest}"

echo "📦 Construyendo imagen: $IMAGE_NAME:$TAG"
docker build -t "$IMAGE_NAME:$TAG" .

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Imagen construida exitosamente!"
    echo ""
    echo "Para ejecutar localmente:"
    echo "  docker run -p 3000:3000 -p 8000:8000 $IMAGE_NAME:$TAG"
    echo ""
    echo "Para acceder a la aplicación:"
    echo "  http://localhost:3000"
    echo ""
    echo "Para subir a Docker Hub:"
    echo "  docker tag $IMAGE_NAME:$TAG TU_USUARIO/$IMAGE_NAME:$TAG"
    echo "  docker push TU_USUARIO/$IMAGE_NAME:$TAG"
else
    echo ""
    echo "❌ Error al construir la imagen"
    exit 1
fi
