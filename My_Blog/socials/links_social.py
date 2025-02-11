import reflex as rx
from My_Blog.components.links_icons import link_icon
import My_Blog.constants.const as const


def link_social() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            link_icon(
                "github",
                const.GITHUB,
                "white"
            ),
            link_icon(
                "mail",
                const.EMAIL,
                "red"
            ),
            link_icon(
                "linkedin",
                const.LINKEDIN,
                "#2196f3"
            )
        )
    )