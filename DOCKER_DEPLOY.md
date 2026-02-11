# Guía de Despliegue - Sitio Estático (Solo Frontend)

> **⚠️ IMPORTANTE**: Este portafolio es un **sitio completamente estático** sin backend.
> No requiere servidor Python ni base de datos en producción, solo archivos HTML/CSS/JS.

## Despliegue Local con Docker

### Construir la imagen
```bash
docker build -t portafolio-majamoci .
```

### Ejecutar el contenedor
```bash
docker run -p 80:80 portafolio-majamoci
```

La aplicación estará disponible en `http://localhost`

## Despliegue en Dokploy (Recomendado)

### Dokploy con Docker

#### Opción 1: Desde Repositorio Git
1. En Dokploy, crea un nuevo proyecto
2. Selecciona "From Git Repository"
3. Conecta tu repositorio de GitHub
4. Dokploy detectará automáticamente el `Dockerfile`
5. Configura el puerto: **80**
6. Despliega

#### Opción 2: Desde Docker Hub
```bash
# Login en Docker Hub
docker login

# Tag de la imagen
docker tag portafolio-majamoci tu-usuario/portafolio-majamoci:latest

# Push a Docker Hub
docker push tu-usuario/portafolio-majamoci:latest
```

Luego en Dokploy:
1. Selecciona "From Docker Image"
2. Ingresa: `tu-usuario/portafolio-majamoci:latest`
3. Puerto: **80**
4. Despliega

## Personalización del Contenido

Para actualizar tu información personal, edita:
```
assets/data/data.json
```

Luego reconstruye y despliega:
```bash
./build.sh
# O reconstruir Docker
docker build -t portafolio-majamoci .
```

## Solución de Problemas

### El puerto 80 ya está en uso (Docker)
```bash
# Cambiar el puerto de mapeo
docker run -p 8080:80 portafolio-majamoci
```

### Reconstruir sin caché
```bash
docker build --no-cache -t portafolio-majamoci .
```

### Error de permisos en build.sh
```bash
chmod +x build.sh
```

### Ver logs del contenedor
```bash
docker logs -f <container_id>
```

## Desarrollo Local (sin Docker)

### Requisitos
- Python 3.12+
- uv (gestor de paquetes rápido)

### Instalación de uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Ejecutar aplicación en modo desarrollo
```bash
# Instalar dependencias
uv sync

# Inicializar Reflex
uv run reflex init

# Ejecutar en modo desarrollo (con hot reload)
uv run reflex run
```

La aplicación estará en `http://localhost:3000`

### Generar build de producción local
```bash
# Generar archivos estáticos
./build.sh

# Probar el build localmente
cd public && python3 -m http.server 8000
```

## Stack Técnico

### Desarrollo
- **Python**: 3.12+
- **Reflex**: 0.8.26+ (solo para generar el frontend)
- **Gestor de Paquetes**: uv
- **Node.js**: Latest (para compilación de frontend)

### Producción (lo que se despliega)
- **HTML/CSS/JavaScript**: Archivos estáticos compilados
- **No requiere**: Backend, base de datos, servidor Python
- **Servido por**: Nginx (Docker) o cualquier servidor de archivos estáticos

## Arquitectura

```
┌─────────────────────┐
│  Código Python      │ (Solo en desarrollo)
│  (Reflex)           │
└──────────┬──────────┘
           │
           │ uv run reflex export
           │ (compilación)
           ▼
┌─────────────────────┐
│  Archivos Estáticos │ ← Esto se despliega
│  HTML/CSS/JS        │
└─────────────────────┘
           │
           │ nginx / servidor estático
           ▼
┌─────────────────────┐
│  Usuario / Browser  │
└─────────────────────┘
```

## Ventajas del Despliegue Estático

✅ **Sin servidor Python en producción**  
✅ **Sin base de datos**  
✅ **Sin websockets**  
✅ **Despliegue con Docker** (Dokploy, VPS, Cloud)  
✅ **Carga ultra-rápida**  
✅ **Costos mínimos**  
✅ **Alta disponibilidad** ✅ **Fácil escalabilidad**
