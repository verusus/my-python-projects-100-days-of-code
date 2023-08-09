from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt='Which turtle will win the race? choose a color: '
                                                          '"red", "orange", "yellow", "green", "blue", "yellow"')
colors = ["red", "orange", "yellow", "green", "blue", "yellow"]

x_start_pos = -230
y_start_pos = 150
all_turtles = []

for turtle_i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_i])
    new_turtle.penup()
    new_turtle.goto(x=x_start_pos, y=y_start_pos)
    y_start_pos -= 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()
