from turtle import Turtle
FONT = ("Courier", 50, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.x_pos = x_pos
        self.goto(x=x_pos, y=250)
        self.score = 0
        self.print_s()

    def print_s(self):
        self.write(arg=f"{self.score}", font=FONT, align=ALIGN)

    def update(self):
        self.clear()
        self.score += 1
        self.print_s()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", font=FONT, align=ALIGN)
