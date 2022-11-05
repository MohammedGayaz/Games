from os import R_OK
from tkinter import Pack
from turtle import Turtle, Screen
from board import Board, ScoreBoard
from ball import Ball
from bat import Paddel
import time

S_WIDTH = 800
S_HEIGH = 800
BG_COLOR = "black"


screen = Screen()
screen.tracer(0)
screen.setup(width=S_WIDTH, height=S_HEIGH)
screen.bgcolor(BG_COLOR)

board = Board()
r_paddel = Paddel((350, 0))
l_paddel = Paddel((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(fun=r_paddel.go_up,key="Up")
screen.onkeypress(fun=r_paddel.go_down,key="Down")
screen.onkeypress(fun=l_paddel.go_up, key='w')
screen.onkeypress(fun=l_paddel.go_down, key='s')

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    
    if ball.distance(r_paddel) < 50 and ball.xcor() > 320 or ball.distance(l_paddel) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360:
        ball.reset_position()
        score.lscore += 1

    if ball.xcor() < -360:
        ball.reset_position()
        score.rscore += 1
    score.update_score()
