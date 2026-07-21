class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

# Car owns the engine and the wheel
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power) # Created a Engine object
        self.wheel = [Wheel(wheel_size) for wheel in range (4)] # Created a Wheel object 4 times
    
    def display_car(self):
        print(f"Your car is a {self.make} {self.model}, with {self.engine.horse_power}hp and an {self.wheel[0].size} inches wheel size.")

car1 = Car("Honda", "Civic", 500, 18)
car1.display_car()