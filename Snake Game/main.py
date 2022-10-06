from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("La Snake")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move(20)

    # Let's detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        time.sleep(2)

    # Detect collision with tail
    for segments in snake.snake[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()
            time.sleep(2)

screen.exitonclick()
