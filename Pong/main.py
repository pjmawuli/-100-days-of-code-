from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard_r = ScoreBoard(40)
scoreboard_l = ScoreBoard(-40)

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 335 or ball.distance(l_paddle) < 50 and ball.xcor() <= -335:
        ball.bounce_x()

    # Detect right paddle miss ball
    if ball.distance(r_paddle) > 50 and ball.xcor() >= 380:
        screen.tracer(0)
        ball.reset_position()
        time.sleep(1.5)
        scoreboard_l.update()

    # Detect left paddle miss ball
    if ball.distance(l_paddle) > 50 and ball.xcor() <= -380:
        screen.tracer(0)
        ball.reset_position()
        time.sleep(1.5)
        scoreboard_r.update()

screen.exitonclick()
