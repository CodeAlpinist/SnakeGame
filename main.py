from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Farzin's Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()

screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.listen()

game_is_0n = True
while game_is_0n:
    snake.keep_going()
    screen.update()
    time.sleep(0.2)

    # Detect collision with food
    if snake.body[0].distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.add_body()

    # Detect collision with wall
    if snake.body[0].xcor() > 280 or snake.body[0].xcor() < -280 or snake.body[0].ycor() > 280 or snake.body[
        0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.body[1:]:
        if snake.body[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
