from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode='r') as f:
            self.high_score = int(f.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(100, 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24,"bold"))
        self.goto(-100, 260)
        with open("high_score.txt", mode='r') as f:
            self.high_score= int(f.read())
        self.write(f"High Score: {self.high_score}", align="center", font=("Arial", 24,"bold"))

    def increase_score(self):
        self.score += 1
        self.update_score() 


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode='w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()


def draw_line(initial_x, initial_y, sethed):
    pen = Turtle()
    pen.speed(0)
    pen.penup()
    pen.goto(initial_x, initial_y)
    cell_gap = 20
    for line in range (27):
        pen.pendown()
        pen.seth(sethed)
        pen.forward(500)
        pen.penup()
        pen.hideturtle()
        if sethed == 0:
            pen.goto(initial_x, initial_y)
            initial_y -= cell_gap            
        else:
            pen.goto(initial_x, initial_y)
            initial_x += cell_gap
            

def draw_grid():
    initial_x = -250
    initial_y = 250
    draw_line(initial_x, initial_y, sethed = 0)
    draw_line(initial_x, initial_y, sethed = 270)
    