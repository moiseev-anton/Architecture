from ..stuff.angle_3d import Angle3D
from ..stuff.color import Color
from ..stuff.point_3d import Point3D


class Flash:
    def __init__(self):
        self.location = Point3D()
        self.angle = Angle3D()
        self.color = Color()
        self.power = 0.0

    def rotate(self, angle_action: Angle3D):
        pass

    def move(self, point_action: Point3D):
        pass
