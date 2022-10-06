from turtle import Turtle
from turtle import Screen
import random

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.color("cyan")

sides = 3
angle = 360
for shape in range(1, 11):
    for x in range(sides):
        timmy.forward(100)
        timmy.right(angle/sides)
    sides += 1
    screen.colormode(255)
    timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen.exitonclick()
