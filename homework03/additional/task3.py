# Переписать код в соответствии с Interface Segregation Principle:

from abc import ABC, abstractmethod
import math


# разделяем интерфейс на 2 отдельных
class Area(ABC):
    @abstractmethod
    def area(self):
        pass


class Volume(ABC):
    @abstractmethod
    def volume(self):
        pass


# Классы фигур теперь реализуют только нужные интерфейсы
class Circle(Area):
    def init(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius


class Cube(Area, Volume):
    def init(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge
