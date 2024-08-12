#Inheritance allows a class to inherit attributes and methods from another class
#helps with code reusability and extensibility 
#class Child(Parent) // also called class Sub(SuperClass)

class Animal:
    def __init__(self, name, num_legs):
        self.name = name
        self.num_legs = num_legs
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    def legs(self):
        print(f"{self.name} has {self.num_legs}")

#children can have their own attributes while inheriting the attributes of Parent class

class Dog(Animal):
    def speak(self):
        print("Woof Woof")
class Cat(Animal):
    def speak(self):
        print("Meow Meow")
class Mouse(Animal):
    def speak(self):
        print("Squeak Squeak")

dog = Dog("Scooby",4)
cat = Cat("Tom", 4)
mouse = Mouse("Jerry", 4)

dog.eat()
dog.legs()
dog.speak()

cat.eat()   
cat.legs()
cat.speak()

mouse.eat()
mouse.legs()
mouse.speak()