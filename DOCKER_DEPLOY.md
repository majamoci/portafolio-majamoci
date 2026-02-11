# Guía de Despliegue con Docker y Dokploy

## Despliegue Local con Docker

### Construir la imagen
```bash
docker build -t portafolio-majamoci .
```

### Ejecutar el contenedor
```bash
docker run -p 3000:3000 -p 8000:8000 portafolio-majamoci
```

La aplicación estará disponible en `http://localhost:3000`

## Despliegue en Dokploy

### Opción 1: Desde Repositorio Git

1. En Dokploy, crea un nuevo proyecto
2. Selecciona "From Git Repository"
3. Conecta tu repositorio de GitHub
4. Dokploy detectará automáticamente el `Dockerfile`
5. Configura los puertos:
   - Puerto Frontend: 3000
   - Puerto Backend: 8000
6. Despliega

### Opción 2: Desde Docker Hub

#### Paso 1: Subir imagen a Docker Hub
```bash
# Login en Docker Hub
docker login

# Tag de la imagen
docker tag portafolio-majamoci tu-usuario/portafolio-majamoci:latest

# Push a Docker Hub
docker push tu-usuario/portafolio-majamoci:latest
```

#### Paso 2: Desplegar en Dokploy
1. En Dokploy, crea un nuevo proyecto
2. Selecciona "From Docker Image"
3. Ingresa: `tu-usuario/portafolio-majamoci:latest`
4. Configura los puertos:
   - Puerto Frontend: 3000
   - Puerto Backend: 8000
5. Despliega

## Variables de Entorno (Opcional)

Si necesitas configurar variables de entorno, añádelas en Dokploy:

```env
REFLEX_ENV=production
```

## Personalización

Para actualizar tu información personal, edita el archivo:
```
assets/data/data.json
```

Luego reconstruye y despliega nuevamente.

## Solución de Problemas

### El puerto 3000 ya está en uso
```bash
# Detener todos los contenedores
docker stop $(docker ps -q)

# O cambiar el puerto de mapeo
docker run -p 8080:3000 -p 8001:8000 portafolio-majamoci
```

### Reconstruir sin caché
```bash
docker build --no-cache -t portafolio-majamoci .
```

## Desarrollo Local (sin Docker)

### Requisitos
- Python 3.12+
- uv (gestor de paquetes rápido)

### Instalación de uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Ejecutar aplicación
```bash
# Instalar dependencias
uv sync

# Inicializar Reflex
uv run reflex init

# Ejecutar en modo desarrollo
uv run reflex run
```

La aplicación estará en `http://localhost:3000`

## Stack Técnico
- **Python**: 3.12+
- **Reflex**: 0.8.26+
- **Gestor de Paquetes**: uv
- **Node.js**: Latest (para compilación de frontend)
