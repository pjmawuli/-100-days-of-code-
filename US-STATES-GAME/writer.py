from turtle import Turtle


class Writer(Turtle):
    def __init__(self):
        super(Writer, self).__init__()
        self.hideturtle()
        self.penup()

    def write_text(self, position, prompt):
        self.goto(position)
        self.write(prompt, align="left", font=("Arial", 10, "normal"))
