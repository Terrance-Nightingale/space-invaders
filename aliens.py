from turtle import Turtle, register_shape

alien_img = "./images/alien.gif"
register_shape(alien_img)


class Aliens(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(alien_img)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)
        self.setpos(0, 200)
