import reflex as rx
from portafolio.data import Extra

from portafolio.styles.styles import IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    return rx.cond(
        len(extra.url) > 0,
        rx.link(
            rx.card(
                rx.inset(
                    rx.image(
                        src=extra.image,
                        height=IMAGE_HEIGHT,
                        width="100%",
                        object_fit="cover"
                    ),
                    pb=Size.DEFAULT.value
                ),
                rx.text.strong(extra.title),
                rx.text(
                    extra.description,
                    size=Size.SMALL.value,
                    color_scheme="gray"
                ),
                width="100%",
                style={
                    "cursor": "pointer",
                    "_hover": {
                        "transform": "translateY(-4px)",
                        "box_shadow": "lg"
                    },
                    "transition": "all 0.2s"
                }
            ),
            href=extra.url,
            is_external=True,
            text_decoration="none"
        ),
        rx.card(
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover"
                ),
                pb=Size.DEFAULT.value
            ),
            rx.text.strong(extra.title),
            rx.text(
                extra.description,
                size=Size.SMALL.value,
                color_scheme="gray"
            ),
            width="100%"
        )
    )
