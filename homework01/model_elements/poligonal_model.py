from ..stuff.point_3d import Point3D
from poligon import Poligon
from texture import Texture


class PoligonModel:
    def __init__(self, textures: list[Texture]):
        self.poligons = []
        self.textures = textures
        self.poligons.append(Poligon([Point3D()]))
