from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)

    def show(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
