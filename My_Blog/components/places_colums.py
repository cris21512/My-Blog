import reflex as rx 
import My_Blog.styles.styles as styles


def places_favorites(title: str, image: str, text: str) -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.text(title, style=styles.title_style,),
            rx.image(
                src=image,
                width="550px",
                height="auto",
                style={
                    "padding_left": "8rem",
                    "_hover": {
                        "transform": "scale(1.1)",
                    },
                }
            ),
            rx.text(text, style=styles.body_style)
        ),
        style={
            "display": "flex",
            "flex_direction": "row",
            "flex_wrap": "wrap",
            "justify_content": "center",
            "align_items": "center",
            "align_content": "center",
            "gap": "85px",
        },
    ),