import time
from turtle import Screen
from ship import Ship
from scoreboard import Scoreboard
from aliens import AlienManager


def update_game_state():
    for alien in aliens.swarm:
        alien.move_right()
        if ship.is_shooting:
            ship.shooting()
        root.update()
    for alien in aliens.swarm:
        alien.move_down()
        if ship.is_shooting:
            ship.shooting()
        root.update()
    for alien in aliens.swarm:
        alien.move_right()
        if ship.is_shooting:
            ship.shooting()
        root.update()
    for alien in aliens.swarm:
        alien.move_down()
        if ship.is_shooting:
            ship.shooting()
        root.update()
    for alien in aliens.swarm:
        alien.move_left()
        if ship.is_shooting:
            ship.shooting()
        root.update()
    for alien in aliens.swarm:
        alien.move_down()
        if ship.is_shooting:
            ship.shooting()
        root.update()
    for alien in aliens.swarm:
        alien.move_left()
        if ship.is_shooting:
            ship.shooting()
        root.update()
    for alien in aliens.swarm:
        alien.move_down()
        if ship.is_shooting:
            ship.shooting()
        root.update()


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

    update_game_state()

    time.sleep(0.03)

root.mainloop()
