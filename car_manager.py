import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


# cars = []

class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def initialize_car(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(1, 2)
        spawn_x = 300
        spawn_y = random.randint(-300, 300)
        new_car.goto(spawn_x, spawn_y)
        self.cars.append(new_car)

    def spawn_car(self):
        pass

    #move all cars in the list of car objects
    def move_car(self):
        for car in self.cars:
            car.forward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT
