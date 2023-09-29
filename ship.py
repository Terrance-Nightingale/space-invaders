from turtle import Turtle, register_shape, Screen
from bullet import Bullet

ship_img = "./images/ship.gif"
register_shape(ship_img)


class Ship(Turtle):

    def __init__(self, screen=Screen):
        super().__init__()
        self.root = screen
        self.can_shoot = True
        self.shape(ship_img)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)
        self.setpos(0, -280)
        # self.lives = []
        # List of current remaining lives. These are turtle objects with ship.gif as the shape.

    def move_left(self):
        current_x = self.xcor()
        if current_x - 45 >= -400:
            self.setx(current_x - 20)

    def move_right(self):
        current_x = self.xcor()
        if current_x + 45 <= 400:
            self.setx(current_x + 20)

    def shoot(self):
        if self.can_shoot:
            bullet = Bullet()
            ship_x = self.xcor()
            bullet.setpos(ship_x, -200)
            self.can_shoot = False
            while bullet.current_y <= 400:
                bullet.move()
                self.root.update()
            if bullet.current_y > 400:
                del bullet
                self.can_shoot = True

    def lose_life(self):
        # Deletes a life from self.lives
        pass
