# Public
class Student:
    def __init__(self):
        self.marks = 80

s = Student()
print(s.marks)

# Proctected
class Student:
    def __init__(self):
        self._marks = 90
    def get_marks(self):
        return self._marks

s = Student()
print(s.get_marks())

# Private
class Student:
    def __init__(self):
        self.__marks = 95

    def get_marks(self):
        return self.__marks
    
# Accessing private directly
s = Student()
# print(s.__marks)

# Accessing private with method
print(s.get_marks())

