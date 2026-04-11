from turtle import Turtle,Screen
import random

puma=Turtle()
puma.pensize(10)
# puma.pencolor("green")
# puma.forward(100)
puma.speed(100)
colors=["red","yellow","blue","green","pink"]

for x in range(100):
    puma.pencolor(random.choice(colors))
    angel=random.randint(0,360)
    random.choice([puma.left,puma.right])(angel)  #angel is out of the function () because first it will choose one left or right then will add the random value to angel 
    number=random.randint(10,100)
    random.choice([puma.forward,puma.backward])(number)
    random.choice(colors)


#we can use setheadding  to pick a random direction direction=0 90 180 270 degree 
