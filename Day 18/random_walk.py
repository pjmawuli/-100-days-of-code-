from turtle import Turtle
from turtle import Screen
import random

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.color("cyan")
timmy.speed(10)

angle = [0, 90, 180, 270]

for x in range(0, 500):
    timmy.pensize(10)
    timmy.forward(40)
    timmy.setheading(random.choice(angle))
    screen.colormode(255)
    timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen.exitonclick()

