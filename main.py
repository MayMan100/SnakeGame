# Import some dependencies
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Intialize some classes and variables
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
game_is_on = True

# Listen to key presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collosion with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update()

    # Detect collosion with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    # Detect collosion with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()