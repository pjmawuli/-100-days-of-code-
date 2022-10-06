from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super(Paddle, self).__init__()
        self.sety(y_pos)
        self.setx(x_pos)
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.speed(10)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def up(self):
        if self.distance(x=350, y=280) < 15 or self.distance(x=-350, y=280) < 15:
            pass
        else:
            self.forward(30)

    def down(self):
        if self.distance(x=350, y=-280) < 15 or self.distance(x=-350, y=-280) < 15:
            pass
        else:
            self.back(30)