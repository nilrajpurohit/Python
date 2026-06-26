# Normal Class
class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

# Dataclass
from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int

s = Student("Nil", 26)
print(s)
