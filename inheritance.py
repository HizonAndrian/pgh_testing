class Animal:
    def __init__(self, type, name):
        self.name = name
        self.type = type

    def eat(self):
        print(f"Animal {self.type} is eating.")

 
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

dog = Dog("Dog", "Billion")
cat = Cat("Cat", "Ticket")

print(f"Dog's name: {dog.name}")
print(f"Cat's name: {cat.name}")

dog.eat()
dog.speak()
cat.eat()
cat.speak()


# https://github.com/HizonAndrian/pgh_testing.git