import reflex as rx
from My_Blog.socials.links_social import link_social
from My_Blog.styles.styles import BASE_STYLE
from My_Blog.components.navbar import navbar
from My_Blog.views.text_cuadro import text_dialog
from My_Blog.Places.lugares import lugares_favoritos
from My_Blog.views.header import cabecera


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            cabecera(),
            navbar(),
            link_social(),
            text_dialog(),
            lugares_favoritos(),
            style={
                "display": "flex",
                "flex_direction": "column",
                "align_items": "center",
                "justify_content": "center",
            },
        ),
        padding_top="0.70rem",
        width="100%",
    ),


app = rx.App(
    style=BASE_STYLE
)
app.add_page(
    index,
    title="Mi blog | Cristopher Fuentes",
    image="https://i.imgur.com/lpgtOqc.jpeg"
    )
