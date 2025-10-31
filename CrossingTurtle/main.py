import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
game_loop = 6
while game_is_on:
    time.sleep(0.1)
    car.bunch_car()
    car.car_move()
    if player.game_win():
        player.starting()
        car.car_speeding()
        scoreboard.update_score()
    for each_car in car.cars:
        if player.distance(each_car) < 20:
            scoreboard.game_over()
            game_is_on = False
    screen.update()

screen.exitonclick()