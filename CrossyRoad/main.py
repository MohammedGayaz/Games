from turtle import Turtle, Screen
from board import Board, ScoreBoard
from chicken import Chicken
from random_car import Car
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")

board = Board()
chicken = Chicken()
car = Car()
score = ScoreBoard()


screen.listen()
screen.onkeypress(key='w', fun=chicken.move_up)
screen.onkeypress(key='s', fun=chicken.move_down)

game_on = True
speed = 0.1

while game_on:
    time.sleep(speed)
    screen.update()
    car.creat_car()
    car.move_cars()

    if chicken.ycor() < -230:
        chicken.goto(0, -230)

    if chicken.ycor() > 230:
        chicken.goto(0, -230)
        speed *= 0.9
        score.level += 1
        score.update_score()

    for each_car in car.cars:
        if chicken.distance(each_car) < 20:
            score.game_over()
            game_on = False

screen.mainloop()
