import random
from turtle import Turtle

class Mouse(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.eaten()

    def eaten(self):
        x_post = random.randint(-280, 280)
        y_post = random.randint(-280, 250)
        self.teleport(x_post, y_post)

