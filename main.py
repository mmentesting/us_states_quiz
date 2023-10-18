import pandas as pd
import turtle
from sticker import Sticker

screen = turtle.Screen()
screen.title("US State Game. Can you name all US states?")
screen.bgpic("blank_states_img.gif")

sticker = Sticker()

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    user_answer = screen.textinput(f"{len(guessed_states)}/50 States Correct",
                                   "Enter a state: \nor\nEnter 'Exit' to Esc").title()
    if user_answer in states:
        if user_answer not in guessed_states:
            row = data[data.state == user_answer]
            position = (int(row["x"]), int(row["y"]))
            sticker.state_sticker(position, user_answer)
            guessed_states.append(user_answer)
    if user_answer == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_df = pd.DataFrame(missing_states)
        new_df.to_csv("remaining_states.csv")
        break

screen.exitonclick()
