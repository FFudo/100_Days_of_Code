import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

P1_START = (-350, 0)
P2_START = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p1 = Paddle(P1_START)
p2 = Paddle(P2_START)
ball = Ball()

screen.listen()
screen.onkeypress(p1.up, "Up")
screen.onkeypress(p1.down, "Down")
screen.onkeypress(p2.up, "w")
screen.onkeypress(p2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

screen.exitonclick()
