from turtle import Screen,Turtle
from snake import Snake   #snake module imported
import time

snake = Snake() # snake object created for class Snake
 # this creation of object will provoke the function __int__ of class Snake
 #where variables will be created and their is 1 function call will activate ie it will call that function where boxes are created



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("pink")
screen.tracer(0) #off the screen
screen.title("SNAKEYYYY")
screen.listen()

screen.onkey(snake.up,"Up") #90
screen.onkey(snake.down,"Down") # 270
screen.onkey(snake.left,"Left") #180
screen.onkey(snake.right,"Right") #0

#snake.up is a function but we are not using () as it is already in a function onkey



gameison=True
while gameison:

    time.sleep(0.1)
    screen.update()
    snake.move_snake()    #from snake module (NOT CLASS) it will call this function



screen.exitonclick()
