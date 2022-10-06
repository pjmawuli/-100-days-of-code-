from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.fd(10)


def move_backward():
    tim.bk(10)


screen.listen()
screen.onkey(key="d", fun=move_forward)
screen.onkey(key="a", fun=move_backward)

screen.exitonclick()
