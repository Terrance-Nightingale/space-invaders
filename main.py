import time
from turtle import Screen
from ship import Ship
from scoreboard import Scoreboard
from aliens import AlienManager

root = Screen()
root.title("Space Invaders")
root.setup(width=800, height=800)
root.bgcolor("black")
root.tracer(0)

scoreboard = Scoreboard()
ship = Ship(root)
aliens = AlienManager()

root.onkeypress(ship.move_left, "Left")
root.onkeypress(ship.move_right, "Right")
root.onkeypress(ship.shoot, "space")
root.listen()

playing = True
while playing:
    root.update()

    for alien in aliens.swarm:
        alien.move()
        root.update()

    time.sleep(0.03)

root.mainloop()
