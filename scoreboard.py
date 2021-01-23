from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-220, 260)
        self.level = 1
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def rst(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
