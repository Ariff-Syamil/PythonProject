from turtle import Turtle

MOVE_FORWARD = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.snake_length = []
        self.create_snake()
        self.head = self.snake_length[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.normal_snake(position)

    def normal_snake(self,position):
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        snake.penup()
        snake.goto(position)
        self.snake_length.append(snake)

    def longer_snake(self):
        self.normal_snake(self.snake_length[-1].position())

    def new_snake(self):
        for each in self.snake_length:
            each.hideturtle()
        self.snake_length = []
        self.create_snake()
        self.head = self.snake_length[0]

    def move(self):
        for segment in range(len(self.snake_length) - 1, 0, -1):
            x_move = self.snake_length[segment - 1].xcor()
            y_move = self.snake_length[segment - 1].ycor()
            self.snake_length[segment].goto(x_move, y_move)
        self.snake_length[0].forward(MOVE_FORWARD)

    def mov_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def mov_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def mov_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def mov_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
