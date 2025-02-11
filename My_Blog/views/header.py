import reflex as rx


def cabecera() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Cristopher Fuentes",
            height="40px",
            width="100%",
            size="8",
            style={
                "font_family": "Ubuntu",
                "color": "#FDB515"
            }
        ),
        position="sticky"
    )