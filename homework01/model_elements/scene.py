from ..model_elements.camera import Camera
from ..model_elements.flash import Flash
from ..model_elements.poligonal_model import PoligonModel


class Scene:
    def __init__(self, id, models: list[PoligonModel], flashes: list[Flash], cameras: list[Camera]):
        self.id = id
        if len(models) > 0:
            self.models = models
        else:
            raise Exception("Должна быть одна модель")
        self.flashes = flashes

        if len(models) > 0:
            self.cameras = cameras
        else:
            raise Exception("Должна быть одна камера")

    def method1(self, value):
        return value

    def method2(self, value, value1):
        return value
