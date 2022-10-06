from turtle import Turtle
FONT = ("Arial", 22, "normal")
ALIGN = "center"

# with open("data.txt", mode="r") as file:
#     HIGHSCORE =

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.print_s()

    def print_s(self):
        self.write(arg=f"Score {self.score}    HighScore: {self.high_score}", font=FONT, align=ALIGN)

    def update(self):
        self.clear()
        self.print_s()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", font=FONT, align=ALIGN)
