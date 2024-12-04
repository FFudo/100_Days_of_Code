import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Guess Game")

image = "./Day25_UsStates/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_states_list = []
df = pd.read_csv("./Day25_UsStates/50_states.csv")
states_list = df["state"].to_list()

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()


while len(correct_states_list) < 50:
    answer_state = screen.textinput(
        title=f"{len(correct_states_list)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    if answer_state == "Exit":
        break
    if answer_state in states_list:
        correct_states_list.append(answer_state)
        correct_row = df[df["state"] == answer_state]
        cords = (correct_row.x.values[0], correct_row.y.values[0])
        tim.goto(cords)
        tim.write(arg=answer_state, align="center", font=("Courier", 8, "normal"))

states_to_learn = []

for state in states_list:
    if state not in correct_states_list:
        states_to_learn.append(state)

df2 = pd.DataFrame(states_to_learn)
df2.to_csv("./Day25_UsStates/states_to_learn.csv")