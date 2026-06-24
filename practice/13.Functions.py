name="Nil"
def greet_name():
    print(name)

greet_name()

def greet(name):
    print(f"Hello {name}")

greet("Alice")

def greet2(name="Guest"):
    print(f"Hello {name}")

greet2()
greet2("John")

def add(*args):
    print(args)
    print(type(args))

add(1, 2, 3, 4)

def add(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print(add(10, 20, 30))

def details(**kwargs):
    print(kwargs)

details(name="Alice", age=25)


def test():
    pass

print(test())
