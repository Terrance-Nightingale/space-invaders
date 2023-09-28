from turtle import Turtle, register_shape


class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_wid=2, stretch_len=0.2)
        self.setpos(0, -100)





