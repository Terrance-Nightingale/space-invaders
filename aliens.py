from turtle import Turtle, register_shape
from bullet import Bullet

BULLET_COLOR = "#02db4b"
alien_img = "./images/alien.gif"
register_shape(alien_img)


class AlienManager:
    def __init__(self):
        self.swarm = []
        self.create_swarm()

    def respawn(self):
        self.swarm = []
        self.create_swarm()

    def create_swarm(self):
        start_x = 15
        y_pos = 275
        for _ in range(0, 4):
            x_pos = -275 + start_x
            for _ in range(0, 8):
                new_alien = Alien(x_pos, y_pos)
                self.swarm.append(new_alien)
                x_pos += 75
            y_pos -= 75
            start_x *= -1


class Alien(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.is_shooting = False
        self.can_shoot = True
        self.bullet = None
        self.penup()
        self.shape(alien_img)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)
        self.setpos(x_pos, y_pos)

    def move_right(self):
        for _ in range(0, 2):
            current_x = self.xcor()
            self.setx(current_x + 5)

    def move_left(self):
        for _ in range(0, 2):
            current_x = self.xcor()
            self.setx(current_x - 5)

    def move_down(self):
        for _ in range(0, 2):
            current_y = self.ycor()
            self.sety(current_y - 0.5)

    def die(self):
        # Deletes the alien object if hit by a bullet.
        pass

    def shoot(self):
        if self.can_shoot:
            self.bullet = Bullet()
            self.bullet.color(BULLET_COLOR)
            self.bullet.seth(270)
            alien_x = self.xcor()
            alien_y = self.ycor()
            self.bullet.setpos(alien_x, alien_y - 30)
            self.is_shooting = True

    def shooting(self):
        if self.can_shoot:
            self.can_shoot = False
        try:
            if self.bullet.current_y >= -400:
                self.bullet.enemy_move()
            else:
                del self.bullet
                self.can_shoot = True
                self.is_shooting = False
        except AttributeError:
            pass
