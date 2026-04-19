import time
import turtle
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# speed_of_cars=0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

scoreboard = Scoreboard()


player=Player()
cars=[]
for x in range(6):
    car=CarManager(x)
    cars.append(car)



screen.listen()
screen.onkey(key="Up",fun=player.move_up)

game_is_on = True
while game_is_on:
    time.sleep(player.speed_of_cars)
    screen.update()
    #move turtles
    for car in cars:
        car.move_car()
        # turtle hit car
        if player.distance(car) < 40:
            game_is_on = False
        #turtle won
        if player.ycor() > 280:
            player.turtle_reach()
            scoreboard.increase_level()




    # screen.update()




