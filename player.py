from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.move_distance = 10
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def up(self):
        self.goto(0, self.ycor() + self.move_distance)

    def rst(self):
        self.goto(0, -280)

    def game_over(self):
        self.move_distance = 0
