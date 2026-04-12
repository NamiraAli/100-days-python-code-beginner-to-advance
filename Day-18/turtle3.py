import turtle
from turtle import Turtle,Screen
import random

puma=Turtle()
turtle.colormode(255)
puma.pensize(10)
# puma.pencolor("green")
# puma.forward(100)
puma.speed(100)
# colors=["red","yellow","blue","green","pink"]
def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

direction=[0,90,180,270]

for x in range(200):
    puma.color(randomcolor())
    angel=random.choice(direction)
    random.choice([puma.left,puma.right])(angel)  #angel is out of the function () because first it will choose one left or right then will add the random value to angel
    number=random.randint(10,100)
    random.choice([puma.forward,puma.backward])(number)
    # randomcolor()


#we can use setheadding  to pick a random direction direction=0 90 180 270 degree
