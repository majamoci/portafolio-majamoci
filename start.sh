#!/bin/bash
set -e

echo "🚀 Iniciando portafolio..."

# Iniciar backend de Reflex en segundo plano
echo "▶ Iniciando backend Reflex en puerto 8000..."
uv run reflex run --env prod --backend-only --backend-host 127.0.0.1 --backend-port 8000 --loglevel warning &
REFLEX_PID=$!

# Esperar a que el backend esté listo
echo "⏳ Esperando al backend..."
for i in $(seq 1 30); do
    if curl -s http://127.0.0.1:8000/ping > /dev/null 2>&1; then
        echo "✅ Backend listo"
        break
    fi
    sleep 2
done

# Iniciar Nginx en primer plano
echo "▶ Iniciando Nginx en puerto 80..."
nginx -g 'daemon off;' &
NGINX_PID=$!

echo "✅ Portafolio disponible en puerto 80"

# Esperar a que cualquiera de los procesos termine
wait -n $REFLEX_PID $NGINX_PID 2>/dev/null || true

# Si uno muere, matar el otro
kill $REFLEX_PID $NGINX_PID 2>/dev/null || true
wait
