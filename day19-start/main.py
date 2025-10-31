import random
import turtle

colors = ["purple","blue","red","yellow","orange","green"]
all_turtles = []

screen = turtle.Screen()
screen.setup(width=500,height=400)
user_guess = screen.textinput(title="Make the bet", prompt="Who would win the turtle race?").lower()

y = -140
inside = 0
for turtles_position in range(0, len(colors)):
    new_turtles = turtle.Turtle("turtle")
    new_turtles.color(colors[inside])
    new_turtles.penup()
    new_turtles.goto(-220, y)
    y += 50
    inside += 1
    all_turtles.append(new_turtles)

race_on = True
while race_on:
    for turtles_ready in all_turtles:
        if turtles_ready.xcor() >= 230:
            print(f"The {turtles_ready.pencolor()} turtle win the race.")
            if user_guess == turtles_ready.pencolor():
                print("You win the bet!")
                race_on = False
            else:
                print("You lose your bet!")
                race_on = False
        else:
            turtles_ready.forward(random.randint(0, 10))



screen.exitonclick()
