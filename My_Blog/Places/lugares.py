import reflex as rx
from My_Blog.components.places_colums import places_favorites
from My_Blog.components.titulo import titulo


def lugares_favoritos() -> rx.Component:
    return rx.vstack(
        titulo("Aqui estan mis lugares favoritos:"),
        places_favorites(
            "Cancun",
            "https://www.worldatlas.com/upload/94/49/83/cancun-mexico-jdross75.jpg",
            """ Me encanta Cancun, es un lugar muy bonito y muy divertido"""
        ),
        places_favorites(
            "Francia",
            "https://emaslight.com/wp-content/uploads/2023/05/Courtesy-of-@GettyImages-1.jpg",
            """Es un deleite visitar francia y comer un buen croissant!"""
        ),
        places_favorites(
            "New York",
            "https://i.natgeofe.com/n/874df281-d3e0-489a-98c0-6b840023b828/newyork_NationalGeographic_2328428.jpg",
            """ La gran manzana! un sueño visitar esta ciudad"""
        ),
        places_favorites(
            "Suiza",
            "https://content.skyscnr.com/m/336ca25e0e427ad2/original/GettyImages-473814924.jpg?resize=1800px:1800px&quality=100",
            """ Naturaleza en su maxima expresion... Suiza es un lugar hermoso"""
        )
    )