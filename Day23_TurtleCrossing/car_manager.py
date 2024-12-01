import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_number = 35
        self.car_pool = []
        self.populate_pool()

    def populate_pool(self):
        for _ in range(self.car_number):
            new_color = random.choice(COLORS)
            new_pos = self.get_new_pos()
            new_car = Car(startpos=new_pos, color=new_color)
            self.car_pool.append(new_car)

    def move_cars(self):
        for car in self.car_pool:
            car.move()
            if car.xcor() < -300:
                car.reset_pos(self.get_new_pos())

    def get_new_pos(self):
        return (random.randint(280, 1150), random.randint(-230, 300))


class Car(Turtle):
    def __init__(self, startpos: tuple, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(1, 1.5)
        self.setheading(180)
        self.movement_speed = STARTING_MOVE_DISTANCE
        self.color(color)
        self.reset_pos(startpos)

    def reset_pos(self, pos: tuple):
        self.goto(pos)

    def move(self):
        self.forward(self.movement_speed)
