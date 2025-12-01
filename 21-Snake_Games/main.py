import time
from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from mouse import Mouse

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
mouse = Mouse()
score = ScoreBoard()

screen.onkey(snake.mov_up,"Up")
screen.onkey(snake.mov_right,"Right")
screen.onkey(snake.mov_left,"Left")
screen.onkey(snake.mov_down,"Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with mouse
    if snake.head.distance(mouse) <= 15:
        mouse.eaten()
        score.score_increase()
        snake.longer_snake()

    # Detect collision with wall
    if (snake.head.pos()[0] > 280 or snake.head.pos()[0] < -300 or
        snake.head.pos()[1] < -280 or snake.head.pos()[1] > 300):
        score.highest_score()
        score.update_score()
        snake.new_snake()


    # Detect collision with tail
    # Detect head collide with tail
    for segment in snake.snake_length[1:]:
        if snake.head.distance(segment) < 10:
            score.highest_score()
            score.update_score()
            snake.new_snake()

screen.exitonclick()