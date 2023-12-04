# Переписать код в соответствии с Dependency Inversion Principle:

from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class PetrolEngine(Engine):
    def start(self):
        print("wroom wroom")


class Car:
    def init(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()
