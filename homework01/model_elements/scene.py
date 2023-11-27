from ..model_elements.camera import Camera
from ..model_elements.flash import Flash
from ..model_elements.poligonal_model import PoligonModel


class Scene:
    def __init__(self, id, models: list[PoligonModel], flashes: list[Flash], cameras: list[Camera]):
        self.id = id
        self.models = models
        self.flashes = flashes
        self.cameras = cameras

    def method1(self, value):
        return value

    def method2(self, value, value1):
        return value
