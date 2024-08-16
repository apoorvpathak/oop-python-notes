# Polymorphism = Greek word that means "to have many forms or faces"
#                 poly = many
#                 morphe = form

#                 Two ways to achieve it :
#                 1. Inheritance: An object could be created of the same type as the parent class
#                 2. "Duck Typing": Object must have necessary attributes or methods

from abc import ABC, abstractmethod
class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r **2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2
class Triangle(Shape):
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5
    


# circle = Circle() #here the circle is considered a Circle but also considered a shape, so it has two forms

shapes = [Circle(4), Square(5), Triangle(6, 7)] #each of these objects have two forms

for shape in shapes:
    print(f"{shape.area()} cm^2")