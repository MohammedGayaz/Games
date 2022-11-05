from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "purple"]
COORD = []
for i in range(-210, 230, 20):
    COORD.append(i)

class Car():
    def __init__(self):
        self.cars = []

    def creat_car(self):
        number = random.randint(1, 6)
        if number == 6:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(240, random.choice(COORD))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() <= -220:
                car.goto(10000, 10000)
            else:
                car.seth(180)
                car.forward(5)

        