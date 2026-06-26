class Student:
    student="ABC School"

s1 = Student()
s2 = Student()
print(s1.student)
print(s2.student)

class Animal:
    def speak(self):
        print("Animal Sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()

class Cat(Animal):
    def speak(self):
        print("Meow")

cat = Cat()
cat.speak()

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")

dog = Dog()

# Multiple Inheritance
class A:
    def show(self):
        print("A")
class B:
    def display(self):
        print("B")
class C(A,B):
    pass
c = C()
c.show()
c.display()

# Method Resolution Order
class A:
    def show(self):
        print("A")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
print(B.mro())
print(D.mro())

