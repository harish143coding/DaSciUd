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


answer_state = screen.textinput(title="guess the state", prompt= "what'S the other state name")
print(answer_state)


# coords_df = pd.read_csv("50_states.csv")
# for x,y in coords_df['x', 'y']:
#     map_turtle.goto(x,y)

#

screen.exitonclick()