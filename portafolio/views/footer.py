import reflex as rx
from reflex.style import color_mode
from portafolio.components.media import media
from portafolio.components.dark_mode_toggle import dark_mode_toggle
from portafolio.data import Media
from portafolio.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.hstack(
        rx.cond(
            color_mode == "light",
            rx.image(
                src="/logo-majamoci-negativo.png",
                alt="Logo MAJAMOCI",
                height=["80px", "80px", "100px"],
                width="auto"
            ),
            rx.image(
                src="/logo-majamoci.png",
                alt="Logo MAJAMOCI",
                height=["80px", "80px", "100px"],
                width="auto"
            )
        ),
        rx.spacer(),
        media(data),
        dark_mode_toggle(),
        spacing=Size.DEFAULT.value,
        align="center",
        width="100%",
        flex_wrap=["wrap", "wrap", "nowrap"],
        justify="start"
    )
