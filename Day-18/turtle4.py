import turtle
from turtle import Turtle,Screen
import random

puma=Turtle()
turtle.colormode(255) #we need to import colormode to use puma.color and random color function
puma.speed("fastest")
puma.pensize(2)
current_head=puma.heading()
def sizegap():
    size_of_gap = 5 #can change the value as required
    return size_of_gap
def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

for x in range(int(360/sizegap())): #36 because 360 is the total degree and we are consuming 10 for every circle
    # therefore 360/10 =36 from sizegap()
    puma.color(randomcolor())
    puma.circle(70) # 70 is the radius
    # puma.setheading(current_head+10*x)
    # puma.left(10)
    puma.setheading(puma.heading()+sizegap())


screen = Screen()
screen.exitonclick()
