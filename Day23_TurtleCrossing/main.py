import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_foward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    if player.is_at_finish():
        player.reset_pos()
        car_manager.level_up()
        score.update_score()

    for car in car_manager.car_pool:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()
