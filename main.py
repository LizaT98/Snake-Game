# steps
# 1. Create snake's body that moves forward
# 2. Make the snake moves depending on user inputs
# 3.create random dots (food)
# 4. Keep track of the score
# 4. Make the snake grow as it eats food
# 5. Set up game over if the snake hits a wall or its tail

import turtle
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score, ALIGNMENT
import time
turtle.colormode(255)

snake = Snake()
food = Food()
score = Score()

screen = Screen()
screen.setup(500, 400)
screen.bgcolor("black")
screen.title("Welcome to Snake Game!")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

is_moving = True
while is_moving:
    screen.update()
    time.sleep(0.1) # refreshes the screen
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_points()

    if snake.head.xcor()>245 or snake.head.xcor() < -245:
        score.reset()
        snake.reset_snake()

    elif snake.head.ycor()>200 or snake.head.ycor() < -200:
        score.reset()
        snake.reset_snake()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment)< 5:
            score.reset()
            snake.reset_snake()


screen.exitonclick()


