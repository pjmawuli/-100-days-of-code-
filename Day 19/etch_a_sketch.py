from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.fd(10)


def move_backward():
    tim.bk(10)


def rotate_l():
    tim.left(5)


def rotate_r():
    tim.right(5)


def clear_r():
    tim.penup()
    tim.home()
    screen.reset()
    tim.pendown()


screen.listen()
screen.onkey(key="d", fun=move_forward)
screen.onkey(key="a", fun=move_backward)
screen.onkey(key="w", fun=rotate_r)
screen.onkey(key="s", fun=rotate_l)
screen.onkey(key="c", fun=clear_r)
screen.exitonclick()
