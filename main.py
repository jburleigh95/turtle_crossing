from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkeypress(player.move, 'Up')

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move()
    if loop_count % 6 == 0:
        car_manager.make_car()

    if player.ycor() >= 300:
        player.next_level()
        car_manager.add_speed()
        scoreboard.update_score()

    for car in car_manager.cars:
        if player.distance(car) < 15:
            scoreboard.end_game()
            game_is_on = False

    loop_count += 1

screen.exitonclick()
