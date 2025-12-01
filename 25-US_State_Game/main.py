import turtle
import pandas
FONT = ("Courier", 24, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

guess_state = []
while len(guess_state) < 50 :
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 States Correct",
                                    prompt="What's the state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guess_state]
        # missing_states = []
        # for state in states:
        #     if state not in guess_state:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state not in guess_state and answer_state in states:
        guess_state.append(answer_state)
        state_location = turtle.Turtle()
        state_location.hideturtle()
        state_location.color("black")
        state_location.penup()
        state_data = data[data.state == answer_state]
        state_location.goto(x=state_data.x.item(), y=state_data.y.item())
        state_location.write(answer_state)