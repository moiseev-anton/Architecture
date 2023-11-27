from i_model_changer import IModelChanger
from i_model_changed_observer import IModelChangedObserver

from ..model_elements.camera import Camera
from ..model_elements.flash import Flash
from ..model_elements.poligonal_model import PoligonModel
from ..model_elements.scene import Scene


class ModelStore(IModelChanger):
    def __init__(self, change_observers: list[IModelChangedObserver]):
        self.change_observers = change_observers
        self.models = [PoligonModel(textures=[])]
        self.flashes = [Flash()]
        self.cameras = [Camera()]
        self.scenes = [Scene(0, self.models, self.flashes, self.cameras)]

    def get_scena(self, id) -> Scene:
        for scene in self.scenes:
            if scene.id == id:
                return scene
        return None

    def notify_change(self, sender) -> None:
        return super().notify_change(sender)
