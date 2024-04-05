import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

# for i in range(10):
#     car_manager.initialize_car()

screen.listen()
screen.onkey(player.go_up, "Up")

random_spawn_chance = 8

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    spawn_roll = random.randint(0, 10)
    if spawn_roll > random_spawn_chance:
        new_car = car_manager.initialize_car()
    car_manager.move_car()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.starting_position()
        car_manager.level_up()
        scoreboard.increase_level()













screen.exitonclick()

