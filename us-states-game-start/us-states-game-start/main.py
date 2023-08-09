import turtle
import pandas
import csv

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()


def write_answer(state_answer, coordinates):
    tim.goto(coordinates)
    tim.write(state_answer)


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_list = []

while len(guessed_list) < 50:
    state_num = len(guessed_list)
    answer = screen.textinput(title=f"[{state_num}/50] States Correct", prompt="What's the name of another state?").title()

    if answer == "Exit":
        break
    if answer in states_list:
        # write answers on the map
        state_data_row = data[data.state == answer]
        coordinates = (int(state_data_row.x), int(state_data_row.y))
        write_answer(state_data_row.state.item(), coordinates)
        if answer not in guessed_list:
            guessed_list.append(answer)

# generate a states_to_learn.csv file
not_guessed_list = [state for state in states_list if state not in guessed_list]
# not_guessed_list = []
# for item in states_list:
#     if item not in guessed_list:
#         not_guessed_list.append(item)

new_data = pandas.DataFrame(not_guessed_list)
new_data.to_csv("states_to_learn.csv")
    # screen.mainloop()
    # screen.exitonclick()
