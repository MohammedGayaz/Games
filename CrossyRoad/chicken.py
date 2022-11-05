from turtle import Turtle

class Chicken(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.goto(0,-230)

    def move_up(self):
        self.seth(90)
        self.forward(20)
    
    def move_down(self):
        self.seth(270)
        self.forward(20)

