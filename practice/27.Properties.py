# Property and Setters

class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value

c = Circle(10)
print(c.radius)
c.radius = 20
print(c.radius)

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Invalid name")
        self._name = value

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Invalid age")
        self._age = value

p = Person("Nil", -26)
print(p._name)
print(p._age)
p.age = 26
p.name = "Nilesh"
print(p)
