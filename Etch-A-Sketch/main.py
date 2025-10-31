import turtle
from turtle import Turtle

teo = turtle.Turtle()
teo.speed("fast")

def mov_forward():
    teo.forward(10)

def mov_backward():
    teo.backward(10)

def mov_right():
    teo.right(10)

def mov_left():
    teo.left(10)

def clear():
    teo.clear()
    teo.penup()
    teo.home()
    teo.pendown()

screen = turtle.Screen()
screen.listen()
screen.onkey(mov_forward, "Up")
screen.onkey(mov_backward, "Down")
screen.onkey(mov_right, "Right")
screen.onkey(mov_left, "Left")
screen.onkey(clear, "c")


screen.exitonclick()