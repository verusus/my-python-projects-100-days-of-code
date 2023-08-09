# import turtle
# from turtle import Turtle, Screen
#
#
# timmy = Turtle()
# timmy.color("pink")
# print(timmy)
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.right(25)
# timmy.forward(150)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.border = False
print(table)

