from turtle import Screen,Turtle
from snake import Snake   #snake module imported
from food import Food
from scoreboard import ScoreBoard
import time



screen=Screen()
screen.tracer(0) #off the screen

snake = Snake() # snake object created for class Snake
 # this creation of object will provoke the function __int__ of class Snake
 #where variables will be created and their is 1 function call will activate ie it will call that function where boxes are created
food=Food()
scoreboard = ScoreBoard()


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

    if snake.head.distance(food) <15:  #food
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #detect collison with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        gameison=False
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segment[1:]:
       if snake.head.distance(segment)<10:
            gameison=False
            scoreboard.game_over()

screen.exitonclick()



#slicing : a list
#list[2:5]
