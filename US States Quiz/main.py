import turtle
import pandas

t = turtle.Turtle()

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Games")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
x_cors = data.x.to_list()
y_cors = data.y.to_list()


def first_question():
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    answer = answer_state.title()
    return answer


def next_question():
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="What's another state's name?")
    answer = answer_state.title()
    return answer


correct_answers = 0
correct_list = []
title_answer = first_question()

while correct_answers < 50:

    if title_answer in states:
        correct_answers += 1
        i = states.index(title_answer)
        correct_list.append(states[i])
        x = x_cors[i]
        y = y_cors[i]
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(states[i])
        title_answer = next_question()

    elif title_answer == "Exit":
        states_not_guessed = [state for state in states if state not in correct_list]
        df = pandas.DataFrame(states_not_guessed)
        df.to_csv("states_to_learn")
        break

    else:
        title_answer = next_question()
