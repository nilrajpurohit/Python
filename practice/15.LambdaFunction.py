square = lambda x: x * x
print(square(5))

students = [
    ("John", 90),
    ("Alice", 80),
    ("Bob", 95)
]

students.sort(key=lambda x: x[0])
print(students)
students.sort(key=lambda x: x[1])
print(students)

# Multiple Arguments

add = lambda a, b: a + b

print(add(10, 20))