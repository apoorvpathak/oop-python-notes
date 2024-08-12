# multiple inheritance = inherit from more than one parent class 
# C(A,B)

# multilevel inheritance = inherit from a parent which inherits from another parent

# C(B) <- B(A) <- A

class Animal: #grandparent(just for understanding)
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f" {self.name} is eating")
    def sleep(self):
        print(f" {self.name} is sleeping")


class Prey(Animal): #parent
    def flee(self):
        print(f" {self.name} is fleeing")

class Predator(Animal): #parent
    def hunt(self):
        print(f" {self.name} is hunting")

class Rabbit(Prey): #child
    pass
class Hawk(Predator): #child
    pass
class Fish(Prey, Predator): #child
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.hunt()
fish.flee()

# rabbit.hunt() #throw an error

rabbit.flee()

# hawk.flee()
hawk.hunt()

hawk.eat()
rabbit.sleep()

fish.sleep()