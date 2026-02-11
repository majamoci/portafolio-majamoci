#!/usr/bin/env python3
"""Post-build SEO injection for Reflex SPA export.

Este script modifica el index.html generado por Reflex para inyectar:
- Meta tags SEO (title, description, canonical)
- Open Graph tags (property, no name)
- Twitter Card tags
- JSON-LD structured data (Person schema)
- lang="es" en lugar de lang="en"
- theme-color y preconnect para rendimiento
"""
import json
import sys
from pathlib import Path
from datetime import datetime

SITE_URL = "https://majamoci.dev"


def load_data():
    """Carga los datos del portafolio desde data.json."""
    data_path = Path(__file__).parent / "assets" / "data" / "data.json"
    with open(data_path, encoding="utf-8") as f:
        return json.load(f)


def build_meta_tags(data):
    """Construye las meta tags SEO y Open Graph."""
    title = data["title"]
    description = data["description"]
    image_url = f"{SITE_URL}{data['image']}"
    
    return f"""
    <title>{title}</title>
    <meta name="description" content="{description}"/>
    <meta name="author" content="{data['name']}"/>
    <link rel="canonical" href="{SITE_URL}/"/>
    <link rel="icon" type="image/png" href="/favicon.png"/>

    <!-- Open Graph -->
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="{title}"/>
    <meta property="og:description" content="{description}"/>
    <meta property="og:image" content="{image_url}"/>
    <meta property="og:url" content="{SITE_URL}/"/>
    <meta property="og:locale" content="es_EC"/>
    <meta property="og:site_name" content="{data['name']} - Portafolio"/>

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:title" content="{title}"/>
    <meta name="twitter:description" content="{description}"/>
    <meta name="twitter:image" content="{image_url}"/>

    <!-- SEO & Performance -->
    <meta name="robots" content="index, follow"/>
    <meta name="theme-color" content="#14192D"/>
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin/>
"""


def build_json_ld(data):
    """Construye el JSON-LD structured data (Person schema)."""
    json_ld = {
        "@context": "https://schema.org",
        "@type": "ProfilePage",
        "dateCreated": datetime.now().isoformat(),
        "dateModified": datetime.now().isoformat(),
        "mainEntity": {
            "@type": "Person",
            "name": data["name"],
            "jobTitle": data["skill"],
            "description": data["about"],
            "email": f"mailto:{data['media']['email']}",
            "url": SITE_URL,
            "image": f"{SITE_URL}{data['image']}",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": data["location"].split(",")[0].strip(),
                "addressCountry": "EC"
            },
            "sameAs": [
                data["media"]["github"],
                data["media"]["likedin"]
            ],
            "alumniOf": {
                "@type": "EducationalOrganization",
                "name": "Universidad de las Fuerzas Armadas ESPE"
            },
            "knowsAbout": [tech["name"] for tech in data["technologies"]],
            "worksFor": {
                "@type": "Organization",
                "name": "InQidea Soluciones Digitales"
            }
        }
    }
    
    json_str = json.dumps(json_ld, ensure_ascii=False, indent=2)
    return f'    <script type="application/ld+json">\n{json_str}\n    </script>'


def inject_seo(html_path: Path, data: dict):
    """Inyecta SEO en el HTML generado por Reflex."""
    if not html_path.exists():
        print(f"❌ Archivo no encontrado: {html_path}")
        return False
    
    html = html_path.read_text(encoding="utf-8")
    
    # 1. Cambiar lang="en" a lang="es"
    html = html.replace('lang="en"', 'lang="es"')
    
    # 2. Construir tags SEO
    meta_tags = build_meta_tags(data)
    json_ld = build_json_ld(data)
    
    # 3. Inyectar después de <meta charset>
    if '<meta charSet="utf-8"/>' in html:
        html = html.replace(
            '<meta charSet="utf-8"/>',
            f'<meta charSet="utf-8"/>\n{meta_tags}\n{json_ld}'
        )
    elif '<meta charset="utf-8"/>' in html:
        html = html.replace(
            '<meta charset="utf-8"/>',
            f'<meta charset="utf-8"/>\n{meta_tags}\n{json_ld}'
        )
    else:
        print("⚠️  No se encontró <meta charset>, inyectando después de <head>")
        html = html.replace('<head>', f'<head>\n{meta_tags}\n{json_ld}')
    
    # 4. Escribir el HTML modificado
    html_path.write_text(html, encoding="utf-8")
    
    print(f"✅ SEO inyectado exitosamente en {html_path}")
    return True


def main():
    """Entry point del script."""
    # Determinar ruta del index.html
    if len(sys.argv) > 1:
        html_path = Path(sys.argv[1])
    else:
        # Buscar en las posibles ubicaciones
        possible_paths = [
            Path("/var/www/html/index.html"),  # Docker
            Path(__file__).parent / ".web" / "build" / "client" / "index.html",  # Build local
            Path(__file__).parent / "public" / "index.html",  # Public
        ]
        
        html_path = None
        for path in possible_paths:
            if path.exists():
                html_path = path
                break
        
        if not html_path:
            print("❌ No se encontró index.html en las ubicaciones esperadas")
            print("Uso: python post-build-seo.py [ruta/al/index.html]")
            sys.exit(1)
    
    # Cargar datos y aplicar SEO
    data = load_data()
    success = inject_seo(html_path, data)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
