from turtle import Turtle

class Board(Turtle):

    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """To let the board/paddle to go up"""
        y_position = self.ycor() + 40
        if self.pos()[1] >= 221:
            y_position = self.ycor()
        self.goto(self.xcor(), y_position)

    def go_down(self):
        """To let the board/paddle to go down"""
        y_position = self.ycor() - 40
        if self.pos()[1] <= -220:
            y_position = self.ycor()
        self.goto(self.xcor(), y_position)
