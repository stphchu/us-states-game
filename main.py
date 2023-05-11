import pandas
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(width=725, height=491)
screen.addshape(image)
turtle.shape(image)

correct_guesses = 0
states_guessed = []

state_name = Turtle()
state_name.pu()
state_name.ht()

states_data = pandas.read_csv("50_states.csv").to_dict(orient="records")
# ----------- Alternative to reading the csv --------------
# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# print(data[data.state == "California"].x)

while correct_guesses < 50:
    answer = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="What's another state's name?").title()
    if answer == "Exit":
        break
    if answer not in states_guessed:
        states_guessed.append(answer)
        for state in states_data:
            if state["state"] == answer:
                correct_guesses += 1
                state_xy = (state['x'], state['y'])
                state_name.goto(state_xy)
                state_name.write(f"{answer}")

with open("./states_to_learn.csv", mode="w") as data:
    for state in states_data:
        if state["state"] not in states_guessed:
            data.write(f"{state['state']}\n")


screen.exitonclick()