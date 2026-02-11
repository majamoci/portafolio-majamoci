import reflex as rx

config = rx.Config(
    app_name="portafolio",
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    # URL placeholder para despliegue estático (no se usa)
    api_url="http://localhost:8000",
)
