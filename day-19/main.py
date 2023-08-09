from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pensize(5)


def forward():
    tim.forward(20)


def backward():
    tim.backward(20)


def clockwise():
    tim.setheading(tim.heading() - 10)


def counter_clockwise():
    tim.setheading(tim.heading() + 10)


def clear():
    tim.home()
    tim.clear()


screen.listen()

screen.onkey(key="W", fun=forward)
screen.onkey(key="S", fun=backward)
screen.onkey(key="D", fun=clockwise)
screen.onkey(key="A", fun=counter_clockwise)
screen.onkey(key="C", fun=clear)

screen.exitonclick()
