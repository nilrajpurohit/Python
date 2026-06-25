# Tuple 
point = (10, 20)
print(point)
print(type(point))
print(point[0])

# Tuple Unpackinge
person = ("John", 25)
name, age = person
print(name)
print(age)

# Named Tuple
from collections import namedtuple
Student = namedtuple("Student", ["name", "age"])
s1 = Student("Alice", 22)
print(s1.name)

