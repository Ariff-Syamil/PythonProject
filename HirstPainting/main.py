import colorgram
import turtle
import random

colors = colorgram.extract('image.jpg',10)
new_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_extract = (r, g, b)
    for rgb in color_extract:
        if r and g and b >= 180:
            pass
        else:
            new_color.append(color_extract)

teo = turtle.Turtle()
teo.speed("fastest")
turtle.colormode(255)
teo.penup()
teo.hideturtle()
start_position = -225
y_position = start_position
teo.teleport(start_position,start_position)
for _ in range(10):
    for _ in range(10):
        random_color = random.choice(new_color)
        teo.dot(20, random_color)
        teo.forward(50)
    y_position += 40
    teo.teleport(start_position,y_position)


screen = turtle.Screen()
screen.colormode(255)
screen.exitonclick()