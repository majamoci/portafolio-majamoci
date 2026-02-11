# 🎯 Arquitectura del Proyecto

## Solo Frontend - Sin Backend

Este proyecto es un **portafolio completamente estático** que **NO requiere backend** en producción.

### ¿Cómo funciona?

```
DESARROLLO (tu computadora)
┌──────────────────────────┐
│ Python + Reflex          │  ← Solo usados para GENERAR archivos
│ uv, Node.js              │
└────────────┬─────────────┘
             │
             │ ./build.sh
             │ (compilación)
             ▼
┌──────────────────────────┐
│ public/                  │
│  ├── index.html          │
│  ├── 404.html            │
│  ├── assets/             │  ← Archivos finales
│  │   ├── *.js            │
│  │   └── *.css           │
│  ├── *.jpg, *.png        │
│  └── data/               │
└────────────┬─────────────┘
             │
             │ Se despliega
             ▼
PRODUCCIÓN (servidor web)
┌──────────────────────────┐
│ Nginx / CDN              │  ← Solo serve archivos estáticos
│ (sin Python, sin BD)     │
└────────────┬─────────────┘
             │
             │ HTTP
             ▼
┌──────────────────────────┐
│ Navegador del Usuario    │
└──────────────────────────┘
```

## Qué se ejecuta donde

### En Desarrollo (tu computadora)
- ✅ Python 3.12
- ✅ Reflex 0.8.26
- ✅ Node.js
- ✅ `uv run reflex run` (servidor de desarrollo)

### En Producción (servidor/hosting)
- ❌ **NO** Python
- ❌ **NO** Reflex
- ❌ **NO** Base de datos
- ❌ **NO** Websockets
- ❌ **NO** Backend API
- ✅ Solo archivos HTML/CSS/JS
- ✅ Nginx o servidor web estático

## Datos del Portafolio

Los datos (tu CV, proyectos, etc.) están en:
```
assets/data/data.json
```

Este archivo JSON se **compila dentro del JavaScript** durante el build.  
No hay llamadas API en producción - todo está pre-renderizado.

## Ventajas de esta Arquitectura

1. **Bajo costo** - Hosting en Docker (Dokploy, VPS económicos)
2. **Ultra rápido** - Sin procesamiento del servidor
3. **100% seguro** - Sin código del servidor que hackear
4. **Siempre disponible** - Archivos estáticos son muy confiables
5. **Fácil mantenimiento** - Solo edita data.json y redespliega

## ¿Cuándo necesitarías backend?

Solo si quisieras agregar:
- Formulario de contacto que envíe emails
- Sistema de comentarios
- Base de datos dinámica
- Autenticación de usuarios
- APIs propias

**Para un portafolio personal: NO necesitas backend** ✅
