import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player for game
player = Player()

# Create scoreboard for game
scoreboard = Scoreboard()

# Create manager for cars
car_manager = CarManager()

screen.onkey(player.up, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.tick()

    screen.update()

    for i in car_manager.cars:

        if (i.xcor() + 20 >= player.xcor() + 10 >= i.xcor() - 20 and
                i.ycor() + 10 >= player.ycor() + 10 >= i.ycor() - 10):
            game_is_on = False
            scoreboard.game_over()
            car_manager.game_over()
            player.game_over()

    if player.ycor() > 280:
        player.rst()
        scoreboard.rst()
        car_manager.new_level()

screen.exitonclick()
