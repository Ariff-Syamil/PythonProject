import random
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.mov_speed = 0.1
        self.setheading(random.randint(45,65) or random.randint(135,115))

    def ball_mov(self):
        """ball move including with collide with upper and lower wall"""
        if self.pos()[1] > 280 and self.pos()[0] < 330 :
            self.setheading(360 - self.heading())
        elif self.pos()[1] < -280 and self.pos()[0] > -330:
            self.setheading(360 - self.heading())
        self.forward(20)

    def paddle_bounce(self):
        self.setheading(360 - (self.heading() + 180))
        self.mov_speed *= 0.9

    def ball_score(self):
        self.teleport(0,0)
        self.mov_speed = 0.1
        self.setheading(self.heading() - 180)