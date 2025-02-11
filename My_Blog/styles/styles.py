from .fonts import fonts as Font
from .colors import Color as color



BASE_STYLE = {
    "background_color": "hsla(0, 0%, 0%, 1)",  # removed semicolon
    "background_image": "radial-gradient(circle at 85% 80%, hsla(266.99999999999983, 1%, 12%, 1) 9%, transparent 55%), "
                    "radial-gradient(circle at 60% 24%, hsla(335.9999999999997, 2%, 22%, 1) 5%, transparent 72%), "
                    "radial-gradient(circle at 24% 7%, hsla(299.00000000000006, 4%, 36%, 0.36) 13%, transparent 68%)",  # removed semicolon, split long string
    "background_blend_mode": "normal, normal, normal"  
}

FADENANIMATED = "animate__animated animate__fadeIn"



STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "/css/styles.css"
]

titulos_especiales = {
    "font_family": Font.TEXT,
    "font_size": "40px",
    "padding_top": "2rem",
    "padding_left": "5rem",
    "color": color.DORADO,
    "_hover": {
        "color": color.ORO,
    }
}

title_style = {
    "font_family": Font.TITLE,
    "padding_left": "16rem",
    "font_size": "45px",
    "color": "#ecdda2",
    "_hover": {
        "color": "#c9b977"
    },
}

body_style = {
    "font_family": Font.BODY,
    "font_size": "20px",
    "color": "#f0ebd7",
    "align": "center",
    "padding_left": "7.5rem",
}