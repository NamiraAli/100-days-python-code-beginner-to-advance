from turtle import Turtle , Screen
import turtle
import random
colorlist=[(100,99,2), (71, 31, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 171), (151, 92, 115), (35, 90, 26), (7, 154, 72), (205, 63, 91), (221, 178, 218), (168, 129, 77), (1, 64, 147), (3, 79, 29), (4, 220, 218), (80, 135, 179), (132, 158, 177), (81, 110, 136), (116, 187, 164), (11, 215, 222), (117, 19, 37), (131, 224, 209), (230, 173, 165), (243, 205, 7)]
#10 by 10 size 20 space 50
puma=Turtle()
turtle.colormode(255)
def createart():
    for x in range(10):
        # r=colorlist[x][0]
        # g=colorlist[x][1]
        # b=colorlist[x][2]
        puma.dot(20,random.choice(colorlist))
        puma.penup()
        puma.forward(50)
    # puma.teleport(-50)

    # puma.setheading(90)
    # puma.forward(50)
    # puma.setheading(180)
    # puma.forward(50)

for  y in range(10):
    createart()
    puma.teleport(-50)
    puma.setheading(90)
    puma.forward(50)
    puma.setheading(0)
    puma.forward(50)
    # # else:
    #     puma.setheading(90)
    #     puma.forward(50)
    #     puma.setheading(0)
    #     puma.forward(50)

screen=Screen()
screen.exitonclick()
