from turtle import Turtle

BULLET_SPEED = 5
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
        self.showturtle()

    def move(self):
        self.current_y = self.ycor()
        self.forward(BULLET_SPEED)

    def enemy_move(self):
        self.current_y = self.ycor()
        self.forward(ENEMY_BULLET_SPEED)

    def hit_alien(self, alien):
        if self.distance(alien) < 60:
            return True

    def hit_ship(self, ship):
        if self.distance(ship) < 30:
            return True
