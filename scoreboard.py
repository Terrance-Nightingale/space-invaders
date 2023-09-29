from turtle import Turtle

FONT = ("System", 30, "normal")
TITLE_FONT = ("System", 50, "normal")


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
        self.goto(0, 320)
        self.write("Space Invaders", align="center", font=TITLE_FONT)
        self.goto(-150, -380)
        self.write(f"Stage: {self.stage}", align="center", font=FONT)
        self.goto(150, -380)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def reset(self):
        # Resets the scoreboard to stage 1 and score 0.
        pass

