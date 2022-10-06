from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super(Car, self).__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.new_x = random.randint(100, 600 + random.randint(20, 50))
        self.new_y = random.randint(-220 - random.randint(40, 60), 210 + random.randint(40, 60))
        self.goto(self.new_x, self.new_y)

    def move(self):
        if self.xcor() < -280:
            self.new_x = random.randint(300, 500)
            self.new_y = random.randint(-250, 250)

        self.new_x -= STARTING_MOVE_DISTANCE
        self.goto(x=self.new_x, y=self.new_y)
