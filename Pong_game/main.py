from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboeard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)  # stop refreshing the screen

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

ball = Ball()
scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()  # updating screen
    time.sleep(ball.move_speed)  # wait 0.1s
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9

    # detect R paddle misses
    if ball.xcor() > 380:
        # reset ball
        # ball.reset()
        # paddle_game()
        ball.reset_position()
        scoreboard.l_point()

    # detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
