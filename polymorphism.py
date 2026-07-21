from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, type, name):
        self.type = type
        self.name = name

    @abstractmethod
    def speak(self):
        print("Nice")

    @abstractmethod
    def skills(self):
        pass

class Dog(Animal):
    def __init__(self, type, name):
        super().__init__(type, name)

    def speak(self):
        print(f"{self.name} said WOOF!")
        super().speak()

    def skills(self):
        print(f"{self.name} can JUMP!")


dog = Dog("Belgian", "Billion")

dog.skills()
dog.speak()
        