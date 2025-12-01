import random
import turtle
from math import degrees
from turtle import Turtle, Screen

theo = Turtle()
turtle.colormode(255)
theo.speed("fastest")
colours = ["blue","lime","cyan","gold","black","purple","orange"]
direction = [0,90,180,270,360]

def random_color():
    """Return random color"""
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

def draw_spiral():
    """Draw Spiral"""
    theo.circle(100)
    theo.left(5)

class Spiral:
    for _ in range(72):
        draw_spiral()
        theo.color(random_color())

def draw_shapes(sides):
    """Build triangle, hexagon and so on (Method2)"""
    degree_change = 360 / sides
    for _ in range(sides):
        theo.forward(100)
        theo.right(degree_change)
# class Draw8Shaped2:
#     for shape_sides_n in range(3,11):
#         theo.color(random.choice(colours))
#         draw_shapes(shape_sides_n)

def random_walk():
    """Build random walk"""
    walk = True
    thick = 10
    theo.speed(10)
    while walk:
        theo.pensize(thick)
        theo.color(random_color())
        theo.forward(30)
        theo.setheading(random.choice(direction))
        thick += 0.05

# class Rectangle:
#     """Build rectangle"""
#     for _ in range(4):
#         for _ in range(10):
#             theo.pendown()
#             theo.forward(10)
#             theo.penup()
#             theo.forward(10)
#         theo.right(90)

# class Draw8Shaped1:
#     """Build triangle, hexagon and so on (Method1)"""
#     sides = 3
#     draw = True
#     while draw:
#         degree = 360/sides
#         theo.color(random_color())
#         for _ in range(sides):
#             theo.forward(100)
#             theo.right(degree)
#         sides += 1
#         if sides == 11:
#             draw = False
#




screen = Screen()
screen.exitonclick()