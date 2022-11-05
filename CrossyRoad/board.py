from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, -240)
        self.draw_board()

    def draw_board(self):
        self.draw_layout()
        self.draw_lanes()

    def draw_layout(self):
        #outer boundry
        self.goto(-250, -250)
        self.pensize(width=5)
        self.pendown()
        self.color("red")
        for _ in range(4):
            self.forward(500)
            self.left(90)
        #inner board
        self.pensize(width=0)
        self.goto(-240,-240)
        self.color("light gray")
        self.begin_fill()
        for _ in range(4):
            self.forward(480)
            self.left(90)
        self.end_fill()
        print(self.pos())

    def draw_lanes(self):
        self.pendown()
        for _ in range(24):
            if _ % 23 == 0:
                self.color("light green")
                self.begin_fill()
                self.draw_rectange()
                self.end_fill()
            self.color("black")
            self.draw_rectange()
            ycord = self.ycor() + 20
            self.goto(self.xcor(), ycord)
            self.seth(0)

    def draw_rectange(self):
        for i in range(4):
            self.pendown()
            self.forward(480)
            self.left(90)
            self.penup()
            self.forward(20)
            self.left(90)   

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.level = 1
        self.goto(-200, 250)
        self.write(f"Level= {self.level}", align="center", font=("Courier", 24, "normal"))

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level= {self.level}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        # self.clear()
        self.color("black")
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 60, "bold"))