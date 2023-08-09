# import colorgram
#
# colors = colorgram.extract('hirstSpotPainting.jpg', 30)
# # print(colors)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple_color = (r, g, b)
#     rgb_colors.append(tuple_color)
#
# print(rgb_colors)
import turtle as turle_module
import random

tim = turle_module.Turtle()
turle_module.colormode(255)

color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176),
              (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49),
              (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86),
              (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162),
              (156, 212, 190), (87, 46, 33), (37, 45, 83)]

tim.penup()
tim.hideturtle()
tim.setpos(-100, -150)

for line in range(10):
    for dot in range(10):
        # rand_color = color_list[random.randint(0, len(color_list) - 1)]
        tim.dot(30, random.choice(color_list))
        tim.forward(50)

    # turtle.reset()
    tim.setpos(tim.xcor() - 500, tim.ycor() + 50)

screen = turle_module.Screen()
# turtle.getscreen()
screen.exitonclick()
