from turtle import Turtle, Screen
import random

FOOD_CORD = [float(x) for x in range(-220, 220, 20)]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.shape("square")
        self.speed("fastest")
        self.gen_random_food()
        
            
    def gen_random_food(self):
        random_x = random.choice(FOOD_CORD)
        random_y = random.choice(FOOD_CORD)
        self.goto(random_x, random_y)

