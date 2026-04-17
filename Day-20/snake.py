from turtle import Turtle


MOVE_DIS=20   #use caps for variables outside class
POS = [(0,0), (-20,0), (-40,0)]  #cordinates of snake from start position  (x,y)
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):    #__init__ function is used to create variables
        self.segment=[]      #segment is a list
        self.create_snake()     #function call
        self.head=self.segment[0]


    def create_snake(self):
        for x in POS:
            puma = Turtle(shape="square")
            puma.color("white")
            puma.penup()
            # puma.setpos(x=xpos[x],y=0)
            puma.goto(x)
            self.segment.append(puma)



    def move_snake(self):
        for x in range(len(self.segment) - 1, 0, -1):  # 3
            new_x=self.segment[x-1].xcor() #2 cordi x
            new_y=self.segment[x-1].ycor() # 2 cord y
            self.segment[x].goto(new_x,new_y) # 3 box move to position og 2nd box cord of 2 used

        self.head.forward(MOVE_DIS)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
