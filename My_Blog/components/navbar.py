import reflex as rx
import My_Blog.styles.styles as styles

def navbar() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            src="https://i.imgur.com/lpgtOqc.jpeg",
            radius="full",
            size="8",
            border="3px solid #19191a",
            style= {
                "@keyframes fadeIn": {
                    "from":{"opacity": 0},
                    "to": {"opacity": 1},
                },
                ".fade-in": {
                    "animation": "fadeIn 1s ease-in-out",
                },
                "margin_top": "10px",
            }
        ),
        class_name="fade-in",
    )