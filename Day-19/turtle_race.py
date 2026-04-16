# object state and instances
import turtle
from turtle import Turtle , Screen
import random
allturtle=[]
# turtle.speed("fast")
# puma=Turtle()
screen=Screen()
screen.setup(width=500,height=400)
userbet=screen.textinput(title="make your bet",prompt="ENTER THE COLOR OF THE TURTLE : ")

colors=["red","green","blue","yellow","black","gray","pink"]
y_pos=[-80,-50,-20,10,40,70,100]

for x in range(0,7):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[x])
    new_turtle.goto(x=-250, y=y_pos[x])
    allturtle.append(new_turtle)

race_on=False
if userbet:
    race_on=True

while race_on:

    for turtle in allturtle:  #here we need to use turtle if we use any other variable it will not work
        if turtle.xcor()>230:    #x cordinate >230
            race_on=False
            winner=turtle.pencolor()
            if winner==userbet:
                print("yes you won !!")
            else:
                print(f"you lost {winner} won ")

        steps = random.randint(1, 10)
        turtle.speed("fast")
        turtle.forward(steps)


screen.exitonclick()
