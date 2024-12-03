import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Guess Game")

image = "./Day25_UsStates/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_states_total = 0
correct_states_list = []
df = pd.read_csv("./Day25_UsStates/50_states.csv")
states_list = df["state"].to_list()


while correct_states_total < 50:
    answer_state = screen.textinput(
        title=f"{correct_states_total}/50 States Correct", prompt="What's another state's name?"
    ).title()
    print(answer_state)
    if answer_state in states_list:
        correct_states_total += 1
        correct_states_list.append(answer_state)


