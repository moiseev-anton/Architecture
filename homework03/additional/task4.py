# Переписать код в соответствии с Liskov Substitution Principle:

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side=0):
        self.side = side

    def set_side(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
