from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5, outline=None)
        self.color("white")
        self.penup()
        self.setpos(position)

        # self.shapesize(stretch_wid=20, stretch_len=100)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
