# Despliegue con Docker - Portafolio Reflex (con Backend)

Este proyecto se despliega con Reflex completo, incluyendo servidor backend para funcionalidades interactivas.

## Arquitectura

El Dockerfile:
- Usa Python 3.12 slim como base
- Instala dependencias del sistema (Node.js, npm, unzip, etc.)
- Usa `uv` para gestión rápida de paquetes Python
- Inicializa Reflex y compila el frontend
- Ejecuta tanto el backend (FastAPI) como el frontend (Next.js)

## Puertos

- **Puerto 3000**: Frontend (Next.js)
- **Puerto 8000**: Backend (FastAPI + WebSockets)

## Construcción de la Imagen

```bash
docker build -t portafolio-majamoci .
```

## Ejecución Local

```bash
docker run -p 3000:3000 -p 8000:8000 portafolio-majamoci
```

Luego accede a `http://localhost:3000`

## Despliegue en Cloud

### Railway

1. Conecta tu repositorio en Railway
2. El Dockerfile será detectado automáticamente
3. Expone el puerto **3000** como puerto principal
4. Railway mapeará automáticamente los puertos necesarios

### Render

1. Crea un nuevo servicio en Render
2. Conecta tu repositorio
3. Selecciona "Docker" como tipo de servicio
4. Puerto: **3000**
5. Despliega

### Dokploy

1. En Dokploy, crea un nuevo proyecto
2. Selecciona "From Git Repository"
3. Conecta tu repositorio
4. Expone los puertos: **3000,8000**
5. Puerto principal: **3000**
6. Despliega

## Variables de Entorno (Opcional)

- `REFLEX_ENV`: Ambiente (production, development)
- `REFLEX_BACKEND_ONLY`: Si es `true`, solo ejecuta el backend
- `REFLEX_FRONTEND_ONLY`: Si es `true`, solo ejecuta el frontend

## Docker Compose

Crea `docker-compose.yml`:

```yaml
version: '3.8'

services:
  portafolio:
    build: .
    ports:
      - "3000:3000"
      - "8000:8000"
    environment:
      - REFLEX_ENV=production
    restart: unless-stopped
```

Ejecuta:

```bash
docker-compose up -d
```

## Características

- ✅ Backend completo con FastAPI
- ✅ WebSockets para interactividad
- ✅ Modo oscuro/claro funcional
- ✅ Hot reload en desarrollo
- ✅ Optimizado para producción

## Personalización

Edita tus datos en:
```
assets/data/data.json
```

Luego reconstruye:
```bash
docker build -t portafolio-majamoci .
```

## Solución de Problemas

### Error: "Cannot connect to server: websocket error"

Asegúrate de que ambos puertos (3000 y 8000) estén expuestos y accesibles.

### Error: "Address already in use"

Libera los puertos:

```bash
lsof -ti:3000,8000 | xargs kill -9
```

### El tema oscuro no funciona

Esto requiere el backend. Verifica que el puerto 8000 esté accesible.

## Desarrollo Local (sin Docker)

### Requisitos
- Python 3.12+
- uv (gestor de paquetes)

### Instalación

```bash
# Instalar uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependencias
uv venv
uv pip install -r pyproject.toml

# Ejecutar
uv run reflex init
uv run reflex run
```

La aplicación estará en `http://localhost:3000`
