from turtle import Turtle


class Frame(Turtle):
    def __init__(self):
        super().__init__()
        # try to make it's shape as a frame :
        self.shape("square")
        self.color("white")
        self.fillcolor("black")
        self.shapesize(26, 30, 5)

        # self.penup()
        # self.goto(-300, -300)
        # self.pencolor("white")
        # self.pendown()
        # for corner in range(4):
        #     self.forward(600)
        #     self.left(90)
        # self.hideturtle()
