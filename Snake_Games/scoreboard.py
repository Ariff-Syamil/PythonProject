from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Currier', 25, 'normal')
FONT2 = ('Currier', 27, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(x=0, y=260)
        self.score = 0
        self.high_score = None
        self.update_score()

    def update_score(self):
        self.clear()
        with open("C:/Users/binid25x/OneDrive - Intel Corporation/Desktop/highest_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font= FONT)

    def highest_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:/Users/binid25x/OneDrive - Intel Corporation/Desktop/highest_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0

    def score_increase(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.teleport(x=0, y=0)
    #     self.color("red")
    #     self.write(arg=f"Game Over\nFinal Score: {self.score}", align=ALIGNMENT, font=FONT2)