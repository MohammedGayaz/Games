from turtle import Screen
import time
import draw_board
from snake import Snake
from food import Food
from draw_board import Score


WIDTH = 600
HEIGHT = 600
BACKGROUNG_COLOR = "light gray"

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BACKGROUNG_COLOR)
screen.tracer(0)

food = Food()
snake = Snake()
score = Score()

screen.listen()
screen.onkey(fun=snake.move_up, key="w")
screen.onkey(fun=snake.move_down, key="s")
screen.onkey(fun=snake.move_front, key="d")
screen.onkey(fun=snake.move_back, key="a")

draw_board.draw_grid()
game_on = True
speed = 0.1

while game_on:
    time.sleep(speed)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 10:
        food.gen_random_food()
        snake.add_segment()
        score.increase_score()
        speed  *= 0.9
    if snake.check_collision(score):
        speed = 0.1
    if snake.body_collision(score):
        speed = 0.1
    