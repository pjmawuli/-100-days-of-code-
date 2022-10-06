from car import Car
import random


class CarManager:
    def __init__(self):
        self.car = []
        self.gen_cars()

    def gen_cars(self):
        for car in range(25):
            new_car = Car()
            self.car.append(new_car)

    def move_cars(self):
        for car in self.car:
            car.move()
