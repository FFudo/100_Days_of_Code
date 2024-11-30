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
screen.onkeypress(p1.up, "w")
screen.onkeypress(p1.down, "s")
screen.onkeypress(p2.up, "Up")
screen.onkeypress(p2.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_y_direction()

    
    if ball.xcor() > 320 and ball.distance(p2) < 50 or ball.xcor() < -320 and ball.distance(p1) < 50:
        ball.change_x_direction()

    screen.update()

screen.exitonclick()
