from turtle import Screen
from board import Board
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800 , height=600)
screen.title("Pong")
screen.tracer(0)

r_board = Board((350, 0))
l_board = Board((-350, 0))
scoreboard = ScoreBoard()
ball = Ball()

screen.listen()
screen.onkey(r_board.go_up,"Up")
screen.onkey(r_board.go_down,"Down")
screen.onkey(l_board.go_up,"w" or "W")
screen.onkey(l_board.go_down,"s" or "S")

game_on = True
while game_on:
    time.sleep(ball.mov_speed)
    ball.ball_mov()
    if (ball.pos()[0] > 320 and ball.distance(r_board) < 50 or
            ball.pos()[0] < -320 and ball.distance(l_board) < 50):
        ball.paddle_bounce()

    if ball.pos()[0] > 410:
        scoreboard.update_score_l_player()
        ball.ball_score()

    if ball.pos()[0] < -410:
        scoreboard.update_score_r_player()
        ball.ball_score()

    screen.update()


screen.exitonclick()