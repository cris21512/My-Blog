import reflex as rx
import My_Blog.styles.styles as styles


def titulo (text: str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.titulos_especiales,
    )