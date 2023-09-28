from turtle import Turtle

FONT = ("System", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.stage = 1
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 330)
        self.write(f"Stage:{self.stage}", align="center", font=FONT)
        self.goto(150, 330)
        self.write(f"Score:{self.score}", align="center", font=FONT)



