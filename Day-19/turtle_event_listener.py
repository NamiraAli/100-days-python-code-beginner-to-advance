import turtle
from turtle import Turtle, Screen
puma=Turtle()
screen=Screen()

#
# def move():
#     puma.forward(20)
# screen.listen()
# screen.onkey(key="space", fun=move) #use key ie we can control the turtle
# #no paranteese to function name here in onkey()
# screen.exitonclick()

def move_forward():
    puma.forward(10)
def move_backward():
    puma.backward(10)
def move_left():
    # puma.left(10)
    new_heading=puma.heading()+10
    puma.setheading(new_heading)
def move_right():
    puma.right(10)
def clear():
   turtle.resetscreen()
   # puma.home()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="space",fun=clear)

screen.exitonclick()
