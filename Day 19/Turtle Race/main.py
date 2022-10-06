import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = turtle.textinput("Make a bet", "Which turtle do you think will win the race? ")
is_race_on = True

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
all_turtles = []

starting_y = 110
for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=starting_y)
    starting_y -= 40
    all_turtles.append(new_turtle)

while is_race_on:

    for turtles in all_turtles:
        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)

        if turtles.xcor() >= 230:
            if turtles.color() == user_bet:
                print(f"Looks like the {turtles.pencolor()} turtle has won the race")
                print(f"\nYou win!!")
                is_race_on = False
            else:
                print(f"Looks like the {turtles.pencolor()} turtle has won the race")
                print("\nYou lose")
                is_race_on = False
screen.exitonclick()
