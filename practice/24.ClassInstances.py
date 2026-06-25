# Common Dunder Methods
# Method	Purpose
# __init__	Constructor
# __str__	Readable string
# __repr__	Debug representation
# __len__	Length
# __add__	+ operator
# __eq__	== operator

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.brand)
print(car2.brand)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person: {self.name}"
        
u = User("Nil", 26)
print(u)

class Person:
    def __repr__(self):
        return "Person('John')"
    
p = Person()
print(repr(p))

class Employee:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)
e = Employee("Nil")
e.display()

# Class Method
class Employee:
    company = "ABCD"
    @classmethod
    def get_company(cls):
        return cls.company
    
e = Employee()
print(e.get_company())

# Static Method
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
print(MathUtils.add(10, 30))