from turtle import Turtle, register_shape

ship_img = "./images/ship.gif"
register_shape(ship_img)


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(ship_img)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)
        self.setpos(0, -200)






