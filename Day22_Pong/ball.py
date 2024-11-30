import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.ball_speed = 10
        self.x_dir = random.choice([-1, 1])
        self.y_dir = 1

    def to_middle(self):
        self.change_x_direction()
        self.teleport(0, 0)
        self.y_dir = random.choice([-1, 1])

    def move(self):
        new_x = self.xcor() + (self.ball_speed * self.x_dir)
        new_y = self.ycor() + (self.ball_speed * self.y_dir)
        self.goto(new_x, new_y)

    def change_y_direction(self):
        self.y_dir *= -1

    def change_x_direction(self):
        self.x_dir *= -1
        self.change_speed()

    def change_speed(self):
        self.ball_speed += random.randint(-5, 5)
        self.ball_speed = min(max(self.ball_speed, 17), 23)
