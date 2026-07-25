from abc import ABC, abstractmethod

# Abstraction
class Animal(ABC):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    @abstractmethod
    def speak(self):
        print(f"{self.name} want to speak!")

# Inheritance
class Dog(Animal):
    def __init__(self, name, type, sound):
        super().__init__(name, type)
        self.sound = sound
    
    def speak(self):
        super().speak()
        print(f"{self.name} says {self.sound}")

dog = Dog("Billion", "Dog", "WOOF!")

dog.speak()

# First test with pushing onto different account.

# Test 2nd push