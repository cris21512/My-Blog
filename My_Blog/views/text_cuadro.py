import reflex as rx
import My_Blog.styles.styles as styles


def text_dialog() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.card(
                rx.text(
                    """ Soy un desarrollador web junior, comprometido con aprender lo necesario
                    para ser un full-stack, tarbajando mas la parte front-end... pero con mis conocimientos
                    del back-end. Ademas, soy un creador de contenido de comida.
                    A continuacion les mostrare mis lugares soñados para viajar...¡Bienvenid@s! """,
                    spacing="1rem",
                ),
            ),
            text_wrap="balance",
            width="100%",
            style={
                "height": "auto",
                "width": "auto",
                "color": "#8c8c8c",
                "border": "2px solid #020202",
                "backgroundColor": "rgba(0, 0, 0, 0.3)",
                "transition": "0.4s",
                "_hover": {
                    "color": "white",
                    "transform": "scale(1.1)",
                },
                "max_width": "26rem",
                "margin_top": "10px",
            },
        ),
    )