from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Vitz(Vehicle):
    def start_engine(self):
        return "small engine"
    def fuel(self):
        return "Use less fuel"

vitz = Vitz()
print(vitz.fuel())
