import turtle
from turtle import Turtle
from turtle import Screen
import random

timmy = Turtle()
screen = Screen()
timmy.shape("classic")
timmy.color("cyan")
timmy.speed("fastest")


def draw_spirograph(n):
    for shape in range(int(360 / n)):
        timmy.circle(100)
        timmy.right(n)
        screen.colormode(255)
        timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

draw_spirograph(6)
screen.exitonclick()
