from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen= Screen()

screen.setup(width=800,height=600)
screen.bgcolor("pink")
screen.title("PONG GAME")

screen.tracer(0)
#it gets the animation to turn off no moving of paddle will be seen
#when it goes from (0,0) to (0,350)
#but if only used tracer(0) it will not show anything paddle whould not be vissible
#so we use update everytime to see the paddle n the screen while game is on


left_paddle=Paddle((-350,0))
right_paddle=Paddle((350,0))
ball = Ball()

scoreboard = Scoreboard()

screen.listen()

def right_movement():
    screen.onkey(fun=right_paddle.goup_r,key="Up")
    screen.onkey(fun=right_paddle.godown_r,key="Down")
def left_movement():
    screen.onkey(fun=left_paddle.goup_l,key="w")
    screen.onkey(fun=left_paddle.godown_l,key="s")

right_movement()
left_movement()

gameison=True
while gameison:
    time.sleep(ball.movespeed)
    screen.update() #to see the paddle
    ball.move()

    #detect collison with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        #need to bounce
        ball.bounce_y()


    #collison with right paddle

    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()


    #if paddle misses the ball
    if ball.xcor()>370:  #when the right paddle misses left paddle score increases
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor()<-370:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
