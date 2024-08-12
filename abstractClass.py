# Abstract class: A class that can not be instantiated on its own; Meant to be subclassed
# They can contain abstract methods, which are declared but have no implementation.
# Benefits of Abstract: 
# 1. Prevents instantiation of the class itself
# 2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("You stop the car")

car = Car()
car.go()
car.stop()

class Bike(Vehicle):
    def go(self):
        print("You ride the bike")
    def stop(self):
        print("You stop the bike")

bike = Bike()
bike.go()
bike.stop()