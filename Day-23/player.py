from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


scoreboard = Scoreboard()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed_of_cars = 0.1
        self.shape("turtle")
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)


    def move_up(self):
        self.penup()
        self.forward(MOVE_DISTANCE)

    def turtle_reach(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.speed_of_cars*=0.9


