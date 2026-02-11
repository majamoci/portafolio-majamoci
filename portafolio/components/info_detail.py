import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title),
                rx.text(info.subtitle),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color_scheme="gray"
                ),
                rx.cond(
                    len(info.technologies) > 0,
                    rx.flex(
                        *[
                            rx.badge(
                                rx.box(class_name=technology.icon),
                                technology.name,
                                color_scheme="gray"
                            )
                            for technology in info.technologies
                        ],
                        wrap="wrap",
                        spacing=Size.SMALL.value
                    )
                ),
                rx.hstack(
                    rx.cond(
                        len(info.url) > 0,
                        icon_button(
                            "link",
                            info.url
                        )
                    ),
                    rx.cond(
                        len(info.github) > 0,
                        icon_button(
                            "github",
                            info.github
                        )
                    )
                ),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        rx.cond(
            len(info.image) > 0,
            rx.image(
                src=info.image,
                alt=info.title,
                height=IMAGE_HEIGHT,
                width="auto",
                border_radius=EmSize.DEFAULT.value,
                object_fit="cover"
            )
        ),
        rx.vstack(
            rx.cond(
                len(info.date) > 0,
                rx.badge(info.date)
            ),
            rx.cond(
                len(info.certificate) > 0,
                icon_button(
                    "shield-check",
                    info.certificate,
                    solid=True
                )
            ),
            spacing=Size.SMALL.value,
            align="end"
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )
