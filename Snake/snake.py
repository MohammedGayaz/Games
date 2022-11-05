from turtle import Turtle
from draw_board import Score

class Snake:
    def __init__(self):
        self.segments = []
        self.create_sanke()


    def create_sanke(self):
        segment = Turtle(shape= "square")
        segment.color("red")
        segment.penup()
        self.segments.append(segment)
        self.head = self.segments[0]


    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.hideturtle()
        self.segments.append(new_segment)


    def clear_segments(self, score):
        for segment in self.segments:
            segment.goto(10000, 10000)
        self.segments.clear()
        self.segments.append(self.head)
        self.head.home()
        score.reset_score()


    def check_collision(self, score):
        if self.head.xcor() < -250 or self.head.xcor() > 250 or self.head.ycor() < -250 or self.head.ycor() > 250:
            self.clear_segments(score)
            return True


    def body_collision(self, score):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                self.clear_segments(score)
                return True


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i-1].pos())
            self.segments[i].showturtle()
        self.head.forward(20)


    def move_up(self):
        if self.head.heading() == 270:
            self.head.seth(270)
        else:
            self.head.seth(90)


    def move_down(self):
        if self.head.heading() == 90:
            self.head.seth(90)
        else:
            self.head.seth(270)


    def move_front(self):
        if self.head.heading() == 180:
            self.head.seth(180)
        else:
            self.head.seth(0)


    def move_back(self):
        if self.head.heading() == 0:
            self.head.seth(0)
        else:
            self.head.seth(180)
            