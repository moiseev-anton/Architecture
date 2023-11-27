from poligon import Poligon
from texture import Texture


class PoligonModel:
    def __init__(self, textures: list[Texture]):
        self.poligons = [Poligon()]
        self.textures = textures
