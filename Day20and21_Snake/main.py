from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = []
snake_gap = 0

for _ in range(3):
    new_turtle = Turtle(shape="square")
