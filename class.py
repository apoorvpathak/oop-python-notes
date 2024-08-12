# a class is a blueprint or template for creating objects (instances). It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.

class Car:
    def __init__(self, model, year, color, forSale):
        self.model = model
        self.year = year
        self.color = color
        self.forSale = forSale
    def drive(self):
        print(f"You drive the {self.color} {self.model}")
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
    def describe(self):
        print(f"this is a {self.color} {self.model} made in {self.year}")

car1 = Car("Mustang", 2024, "red", False)

# print(car1) #this will print the memory address of the object location

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.forSale)

car2 = Car("BatMobile", 2024, "Black", False)
car3 = Car("Corvette", 2023, "Blue", False )
# print(car2)

# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.forSale)

# Attributes: Variables that store the state of an object. They are also known as fields or properties.

# Methods: Functions that define the behavior of an object. They operate on the attributes of the object.

# car2.drive()
# car1.stop()

car1.describe()
car2.describe()
car3.describe()

