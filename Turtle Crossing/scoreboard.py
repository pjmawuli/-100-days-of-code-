from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGN = "left"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(x=-200, y=250)
        self.score = 0
        self.print_s()

    def print_s(self):
        self.write(arg=f"Level: {self.score}", font=FONT, align=ALIGN)

    def update(self):
        self.clear()
        self.score += 1
        self.print_s()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", font=FONT, align=ALIGN)
