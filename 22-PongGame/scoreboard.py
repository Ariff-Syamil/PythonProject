from turtle import Turtle
# ALIGN = "center"
FONT = ("Currier", 25 ,"bold")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.score_l_player()
        self.score_r_player()

    def score(self, x_post, y_post):
        self.teleport(x=x_post, y=y_post)
        self.hideturtle()
        self.color("white")

    def score_r_player(self):
        # self.clear()
        self.score(20,250)
        self.write(arg=f"{self.score1}", font=FONT)

    def score_l_player(self):
        # self.clear()
        self.score(-20, 250)
        self.write(arg=f"{self.score2}", font=FONT)

    def update_score_r_player(self):
        self.score1 += 1
        self.clear()
        self.score_l_player()
        self.score_r_player()

    def update_score_l_player(self):
        self.score2 += 1
        self.clear()
        self.score_l_player()
        self.score_r_player()
