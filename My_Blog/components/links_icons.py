import reflex as rx

def link_icon(icon: str, url: str, hover_color: str) -> rx.Component:
    return rx.link(
        rx.vstack( 
            rx.hstack(
                rx.icon(
                    icon,
                    stroke_width="1",                
                ),
                color="white",
                style={
                    "border": "2px inset white",
                    "borderRadius": "50%",
                    "padding": "10px",
                    "backgroundColor": "rgba(0, 0, 0, 0.3)",
                    "transition": "0.3s",
                    "_hover": {
                        "color": hover_color, 
                        "filter": f"drop-shadow(0px 0px 10px {hover_color})",
                        "transform": "scale(1.1)",
                    },
                    "margin_left": "15px",
                    "margin_top": "10px",
                },
            ),
        ),
        href=url,
        is_external=True,
    )