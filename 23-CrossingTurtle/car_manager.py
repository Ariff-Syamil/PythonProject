import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_INCREMENT
        self.bunch_car()

    def bunch_car(self):
        if random.randint(1,6) == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(x=300, y=random.randint(-250,250))
            self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(self.car_speed)
            print(self.car_speed)

    def car_speeding(self):
        self.car_speed += MOVE_INCREMENT * 0.5