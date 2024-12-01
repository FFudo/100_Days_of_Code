from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-210, 250)
        self.level = 1
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
