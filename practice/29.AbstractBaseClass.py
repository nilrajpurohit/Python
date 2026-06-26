from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
r = Rectangle(10, 20)
print(r.area())

# OOP Pillars
# Pillar	Meaning
# Encapsulation	Hide implementation details and control access to data
# Inheritance	Reuse code from existing classes
# Polymorphism	Same interface, different implementations (e.g., method overriding)
# Abstraction	Expose essential behavior while hiding complexity

