from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        for i in range(30):
            self.cars.append(Car(random.choice(COLORS)))

    def game_over(self):
        for i in self.cars:
            i.set_speed(0)

    def new_level(self):
        for i in self.cars:
            i.set_speed(i.move_speed + MOVE_INCREMENT)

    def tick(self):
        for i in self.cars:
            i.move()


class Car(Turtle):

    def __init__(self, clr):
        super().__init__()
        self.move_speed = 5
        self.color(clr)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(random.randint(-300, 300), random.randint(-220, 260))

    def set_speed(self, mv_speed):
        self.move_speed = mv_speed

    def move(self):
        if self.xcor() > -320:
            self.goto(self.xcor() - self.move_speed, self.ycor())
        else:
            self.goto(random.randint(300, 320), self.ycor())
