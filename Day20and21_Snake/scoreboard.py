from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(0, 250)
        self.highscore = self.read_data()
        self.score = 0
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} Highscore: {self.highscore}",
            align="center",
            font=("Arial", 16, "normal"),
        )

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_data()
        self.score = 0
        self.draw_score()

    def game_over(self):
        self.teleport(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=("Arial", 16, "normal"))

    def update_score(self):
        self.score += 1
        self.draw_score()

    def write_data(self):
        with open("./Day20and21_Snake/data.txt", "w") as f:
            f.write(str(self.highscore))

    def read_data(self):
        with open("./Day20and21_Snake/data.txt", "r") as f:
            return int(f.read())