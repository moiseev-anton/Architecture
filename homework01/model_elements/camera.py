from ..stuff.angle_3d import Angle3D
from ..stuff.point_3d import Point3D


class Camera:
    def __init__(self):
        self.location = Point3D()
        self.angle = Angle3D()

    def rotate(self, angle_action: Angle3D):
        pass

    def move(self, point_action: Point3D):
        pass
