from multiprocessing import set_forkserver_preload
from turtle import Turtle

class Paddel(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        if self.ycor() >= 240:
            self.goto(self.pos())
        else:
            new_y = self.ycor() + 40
            self.goto(x=self.xcor(), y = new_y)

    def go_down(self):
        if self.ycor() <= -240:
            self.goto(self.pos())
        else:
            new_y = self.ycor() - 40
            self.goto(x = self.xcor(), y = new_y)
