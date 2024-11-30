from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_pos):
        super().__init__()
        self.color("white")
        self.set_position(starting_pos)
        self.penup()
        self.shape("square")
        self.turtlesize(5, 1)

    def set_position(self, position: tuple):
        x, y = position
        self.teleport(x=x, y=y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
