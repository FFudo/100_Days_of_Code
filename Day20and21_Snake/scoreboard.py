from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(0, 250)
        self.score = 0
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.teleport(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=('Arial', 16, 'normal'))

    def update_score(self):
        self.score += 1
        self.draw_score()
