from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.board()
        self.line()

    def board(self):
        self.goto(-400, -300)
        self.pendown()
        for _ in range(2):
            self.forward(800)
            self.left(90)
            self.forward(600)
            self.left(90)
    
    #dotted line in middle
    def line(self):
        self.goto(0, -300)
        self.seth(90)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.lscore = 0
        self.rscore = 0
        self.goto(-100, 300)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))

    def update_score(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))
        
