import turtle as t

tim = t.Turtle()
screen = t.Screen()
speed = 10


def move_forward():
    tim.forward(speed)


def move_backward():
    tim.backward(speed)


def turn_right():
    new_heading = tim.heading() - speed
    tim.setheading(new_heading)


def turn_left():
    new_heading = tim.heading() + speed
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.teleport(0, 0)


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
