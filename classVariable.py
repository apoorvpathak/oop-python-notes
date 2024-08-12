#class variable = Shared amaong all instances of a class
#                   Defined outside the constructor
#                 Allow you to share data among all objects created from that class

class Student:
    class_year = 2024 #class variable
    num_students = 0
    def __init__(self, name, age): #constructor
        self.name = name
        self.age = age
        Student.num_students +=1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 32)
student3 = Student("Mr Krabs", 55)
student4 = Student("Squidward", 52)
student5 = Student("Sandy Cheeks", 21)
student6 = Student("Plankton", 105)

print(student1.name)
print(student1.age)
print(Student.class_year) #class variables can be accessed through any object, but it a good practice to access it throgh class name "Student"

print(f"total number of students in graduating class of {Student.class_year} are {Student.num_students}")
