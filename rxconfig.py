import reflex as rx

# Configuración para sitio estático (solo frontend, sin backend)
config = rx.Config(
    app_name="portafolio",
    # Deshabilitar plugins que requieren backend
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
