import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Turtle crossing")

# The player
player = Player()

# The Scoreboard
scoreboard = ScoreBoard()

# The Keys to control the player
screen.onkey(player.move, "Up")

# Let's spawn a car object
cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(player.car_speed)
    for vehicle in cars.car:
        if vehicle.distance(player) < 25:
            scoreboard.game_over()
            time.sleep(2)
            game_is_on = False

    if player.ycor() > 280:
        player.goto(0, -280)
        player.car_speed *= 0.6
        scoreboard.update()

    cars.move_cars()

    screen.update()
