from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import Score
from frame import Frame
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


frame = Frame()
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    score.show()

    snake.move()

    # Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update()

    # Detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
        game_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_on = False

screen.exitonclick()
