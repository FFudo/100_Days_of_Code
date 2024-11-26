import turtle as t
import random 


colors = [
    (202, 164, 110),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]

tim = t.Turtle()
tim.speed(20)
t.colormode(255)
screen = t.Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
vertical_gap = 0

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(50)
    
    vertical_gap += 50
    tim.teleport(0 , vertical_gap)

screen.exitonclick()
    

