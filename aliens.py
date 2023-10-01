from turtle import Turtle, Screen, register_shape

alien_img = "./images/alien.gif"
register_shape(alien_img)


class AlienManager:
    def __init__(self, screen=Screen):
        self.root = screen
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

    def move_swarm(self):
        for alien in self.swarm:
            alien.move_right()
            self.root.update()
        for alien in self.swarm:
            alien.move_down()
            self.root.update()
        for alien in self.swarm:
            alien.move_right()
            self.root.update()
        for alien in self.swarm:
            alien.move_down()
            self.root.update()
        for alien in self.swarm:
            alien.move_left()
            self.root.update()
        for alien in self.swarm:
            alien.move_down()
            self.root.update()
        for alien in self.swarm:
            alien.move_left()
            self.root.update()
        for alien in self.swarm:
            alien.move_down()
            self.root.update()


class Alien(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
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
