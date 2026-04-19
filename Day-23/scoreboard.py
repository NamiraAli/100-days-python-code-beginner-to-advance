from random import random
from turtle import Turtle ,Screen
import random
import turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# CARPOSITION=[(270,-120),(270,-50),(270,20),(270,90),(270,160),(270,250)]
CARPOSITION=[-100,-50,0,50,100,150,200]
MOVESPEED=random.randint(5,10)



class CarManager(Turtle):
    def __init__(self,x):
        super().__init__()
        self.startpos=CARPOSITION[x]
        self.goto(270,self.startpos)
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape("square")
        self.penup()
        # self.newx=CARPOSITION[x][0]
        # self.newy=CARPOSITION[x][1]
        self.goto(270,CARPOSITION[x])


        # self.move_car()


    def move_car(self):
        steps = random.randint(1, 20)
        self.speed("fastest")
        self.backward(steps)
        if self.xcor() < -280:
            self.goto(270,self.startpos)
            self.color(random.choice(COLORS))



    # def increase_speed(self):

