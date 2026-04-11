#turtle package name is turtle graphics
from turtle import Turtle , Screen

puma=Turtle()
puma.shape("turtle")
colors=["cyan", "lime", "deep pink","red","blue","green","navy","yellow","darkgreen","coral"]
totalside=3
puma.screen.bgcolor("pink")

for x in range(5):
    puma.color(colors[x])
    for y in range(totalside):
        puma.forward(100)
        # dottedline()
        puma.right(360/totalside)
    totalside+=1    

screen=Screen()
screen.exitonclick()
