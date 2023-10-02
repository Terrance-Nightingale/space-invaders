from turtle import Turtle, register_shape
from bullet import Bullet

ship_img = "./images/ship.gif"
register_shape(ship_img)


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.bullet = None
        self.can_shoot = True
        self.is_shooting = False
        self.hit = False
        self.shape(ship_img)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)
        self.setpos(0, -280)
        self.lives = []
        self.set_lives()

    def move_left(self):
        current_x = self.xcor()
        if current_x - 45 >= -400:
            self.setx(current_x - 20)

    def move_right(self):
        current_x = self.xcor()
        if current_x + 45 <= 400:
            self.setx(current_x + 20)

    def shooting(self):
        if self.can_shoot:
            self.can_shoot = False
        try:
            if self.bullet.current_y <= 400:
                self.bullet.move()
            else:
                self.bullet.hideturtle()
                del self.bullet
                self.can_shoot = True
                self.is_shooting = False
        except AttributeError:
            pass

    def shoot(self):
        if self.can_shoot:
            self.bullet = Bullet()
            ship_x = self.xcor()
            self.bullet.setpos(ship_x, -200)
            self.is_shooting = True

    def lose_life(self):
        self.lives[-1].hideturtle()
        del self.lives[-1]
        self.hit = False

    def set_lives(self):
        x_pos = 260
        y_pos = -350
        for _ in range(0, 3):
            life = Turtle()
            life.shape(ship_img)
            life.shapesize(stretch_wid=0.1, stretch_len=0.1)
            life.setpos(x_pos, y_pos)
            x_pos += 50
            self.lives.append(life)
