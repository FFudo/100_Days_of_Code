from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.speed = 10
        self.x_dir = 1
        self.y_dir = 1

    def move(self):
        new_x = self.xcor() + (self.speed * self.x_dir)
        new_y = self.ycor() + (self.speed * self.y_dir)
        self.goto(new_x, new_y)