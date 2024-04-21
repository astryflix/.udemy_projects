import time
from turtle import Screen
from turtle_crossing_start.player import Player
from turtle_crossing_start.car_manager import CarManager
from turtle_crossing_start.scoreboard import Scoreboard

# als lvl haalt gaat snelheid en hoeveelheid auto's omhoog

screen = Screen()
screen.setup(width=500, height=45)
screen.tracer(0)
screen.bgcolor(0, 0, 0)

player = Player()
cm = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cm.create_car()
    cm.move_car()

    # detect collision with car
    for car in cm.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful level
    if player.is_at_finish_line():
        player.go_to_start()
        cm.lvl_up()
        scoreboard.increase_level()
        # print(scoreboard)

screen.exitonclick()
