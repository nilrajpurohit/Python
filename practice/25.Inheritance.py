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