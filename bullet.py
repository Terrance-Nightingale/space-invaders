from turtle import Turtle

BULLET_SPEED = 10
ENEMY_BULLET_SPEED = 15


class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.current_y = self.ycor()
        self.shape("square")
        self.penup()
        self.color("yellow")
        self.seth(90)
        self.shapesize(stretch_wid=0.2, stretch_len=1)

    def move(self):
        self.current_y = self.ycor()
        self.forward(BULLET_SPEED)

    def enemy_move(self):
        self.current_y = self.ycor()
        self.forward(ENEMY_BULLET_SPEED)

        # Moves up until it either hits an alien or reaches past the top of the screen.
        # After reaching the end of movement, the bullet instance is deleted.
