from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    # Decorator
    @abstractmethod
    def speak(self):
        pass
    
class Dog(Animal):
    def eat(self):
        print(f"{self.name} is eating")
 
    def speak(self):
        print("WOOF!")

dog = Dog("Billion")


print(dog.name)