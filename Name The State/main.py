from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.tracer(0)
screen.setup(width=725, height=500)
screen.bgpic("blank_states_img.gif")


tim = Turtle()
tim.hideturtle()
tim.penup()

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
game_on = True
coutn = 0
correct_state = 0
marked_states = []

def get_coord(location):
    x_cord = int(location.x)
    y_cord = int(location.y)
    return x_cord, y_cord


while game_on:
    coutn += 1
    state_input = screen.textinput(f"{correct_state}/{len(states)} States Correct", "What's another State's Name?")
    if state_input.title() in states and state_input.title() not in marked_states:
        marked_states.append(state_input.title())
        correct_state += 1
        location = data[data.state == state_input.title()]
        tim.goto(get_coord(location))
        tim.write(state_input.title())

    if coutn == len(states):
        tim.goto(-100,0)
        tim.write("Game Over", font=["",40,"normal"])
        break
    screen.update()

# screen.mainloop()
