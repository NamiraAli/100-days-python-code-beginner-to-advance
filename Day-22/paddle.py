from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        # self.paddle = Turtle(shape="square")
        self.shape("square")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def goup_r(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def godown_r(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def goup_l(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def godown_l(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
