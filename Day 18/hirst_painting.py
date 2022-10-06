from turtle import Screen
from turtle import Turtle
import random

tim = Turtle()
screen = Screen()
tim.color("cyan")
tim.speed("fastest")
print(screen.screensize())
tim.penup()
tim.goto(-310, -300)


def line_dot():
    for dots in range(10):
        tim.pendown()
        tim.dot(35)
        tim.penup()
        tim.forward(70)
        screen.colormode(255)
        tim.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))


def move_line():
    tim.goto(-310, tim.ycor() + 60)


for line in range(11):
    line_dot()
    move_line()

screen.exitonclick()
