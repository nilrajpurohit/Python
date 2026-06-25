student = {
    "name": "John",
    "age": 20
}

print(student)
print(student["name"])
print(student.get("age"))

student["name"] = "Nil"
print(student["name"])

for key, value in student.items():
    print(key, ":", value)

square = {x * x for x in range(5)}
print(square)

# Default Dictionaries
from collections import defaultdict
d = defaultdict(int)
d["apple"] += 1
print(d)

# Counter Dictionaries
from collections import Counter
text = "banana"
count = Counter(text)
print(count)
