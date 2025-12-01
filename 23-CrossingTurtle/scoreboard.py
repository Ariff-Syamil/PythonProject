from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=-140,y=260)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg= f"Level: {self.score}", align= "right", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over\nScore: {self.score}", align="center", font=FONT)