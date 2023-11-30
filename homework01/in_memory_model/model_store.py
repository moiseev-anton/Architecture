from i_model_changer import IModelChanger
from i_model_changed_observer import IModelChangedObserver

from ..model_elements.camera import Camera
from ..model_elements.flash import Flash
from ..model_elements.poligonal_model import PoligonModel
from ..model_elements.scene import Scene


class ModelStore(IModelChanger):
    def __init__(self, change_observers: list[IModelChangedObserver]):
        self.__change_observers = change_observers
        self.models = []
        self.flashes = []
        self.cameras = []
        self.scenes = []

        self.models.append(PoligonModel(textures=[]))
        self.flashes.append(Flash())
        self.cameras.append(Camera())
        self.scenes.append(Scene(0, self.models, self.flashes, self.cameras))

    def get_scene(self, id) -> Scene:
        for scene in self.scenes:
            if scene.id == id:
                return scene
        return None

    def notify_change(self, sender) -> None:
        return super().notify_change(sender)
