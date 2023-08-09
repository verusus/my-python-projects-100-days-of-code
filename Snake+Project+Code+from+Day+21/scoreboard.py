from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.high_score = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def get_high_score(self):
        with open("../../Desktop/Data.txt") as file:
            self.high_score = int(file.read())

    def update_scoreboard(self):
        self.clear()
        self.get_high_score()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def set_if_high_score(self):
        if self.score > self.high_score:
            with open("C:/Users/Administrator/Desktop/Data.txt", "w") as high_score:
                high_score.write(f"{self.score}")
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
