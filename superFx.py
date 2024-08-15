# super() = function used in a child(sub) class to call methods from a parent class(superclass).
#             Allows you to extend the functionality of the inherited methods

#super class
class Shape: 
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled'if self.is_filled else 'not filled.'}")

#sub class
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        print(f"The area of the circle is {3.14*self.radius*self.radius} cm^2") #THIS IS METHOD OVERRIDING, THE DESCRIBE METHOD OF THE PARENT WONT BE USED HERE, TO USE THE PARENT TOO, WE WOULD HAVE TO USE THE SUPER FUNCTION
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("red", True, 5)

# print("Circle Color", circle.color)
# print("Circle Radius", circle.radius)
# print("Is it filled", circle.is_filled)

square = Square("Blue", True, 7)

# print("Square Color", square.color)
# print("Square Width", square.width)
# print("Square Length", square.width)
# print("Is it filled", square.is_filled)

triangle = Triangle("Yellow", is_filled=False, width=8, height=7)

# print("Triangle Color", triangle.color)
# print("Triangle Width", triangle.width)
# print("Triangle Height", triangle.height)
# print("Is it filled", triangle.is_filled)

circle.describe()
square.describe()
triangle.describe()