import turtle as t
import random


t.colormode(255)
tim = t.Turtle()


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


#
#
# tim.speed(100)
# directions = [0, 90, 180, 270]
#
#
# def random_step():
#     rand_angle = random.choice(directions)
#     tim.setheading(rand_angle)
#     tim.forward(30)
#
#
# tim.pensize(15)
# for step in range(100):
#     tim.pencolor(rand_color())
#     random_step()

tim.speed("fastest")


def draw_spirograph(shift_degree):
    for number in range(int(360 / shift_degree)):
        tim.pencolor(rand_color())
        tim.circle(100)
        tim.setheading(tim.heading() + shift_degree)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
