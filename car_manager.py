from turtle import Turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
MOVE_INCREMENT = 1.5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = 5
        self.cars = []
        # for _ in range(20):

    def make_car(self):
        car = Turtle('square')
        car.color(random.choice(colors))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        x_start = 0
        y_start = random.randint(-250, 250)
        car.goto((x_start, y_start))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())
            # if car.xcor() <= -300:
            #     self.add_car()
            #     car.goto(self.x_start, self.y_start)

    # def add_car(self):
    #     self.color(random.choice(colors))
    #     self.x_start = 300
    #     self.y_start = random.randint(-260, 260)

    def add_speed(self):
        self.car_speed += MOVE_INCREMENT
