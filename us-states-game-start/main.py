import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)

map_turtle = turtle.Turtle()
turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) <= 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/guess the state",
                                    prompt="what'S the other state name").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    else:
        pass


# coords_df = pd.read_csv("50_states.csv")
# for x,y in coords_df['x', 'y']:
#     map_turtle.goto(x,y)

#

screen.exitonclick()