from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0

    def update_scoreboard(self):
        self.clear()
        self.teleport(-100, 200)
        self.write(self.p1_score, align="center", font=("Courier", 80, "normal"))
        self.teleport(100, 200)
        self.write(self.p2_score, align="center", font=("Courier", 80, "normal"))
