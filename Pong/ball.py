from msilib.schema import Directory
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1
        
    def move_ball(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(x = new_x, y = new_y)

    def bounce_y(self):
        self.ymove *= -1
    
    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.xmove *= -1
        self.move_speed = 0.1