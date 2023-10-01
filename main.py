import time
from random import randint
from turtle import Screen
from ship import Ship
from scoreboard import Scoreboard
from aliens import AlienManager, Alien


def select_alien():
    position = randint(0, len(aliens.swarm) - 1)
    shooter = aliens.swarm[position]
    shooter.shoot()


def check_shoot_state(alien=Alien):
    if alien.is_shooting:
        alien.shooting()
    if ship.is_shooting:
        ship.shooting()


def move_aliens_down():
    for alien in aliens.swarm:
        alien.move_down()
        check_shoot_state(alien)
        root.update()


def move_aliens_right():
    for alien in aliens.swarm:
        alien.move_right()
        check_shoot_state(alien)
        root.update()


def move_aliens_left():
    for alien in aliens.swarm:
        alien.move_left()
        check_shoot_state(alien)
        root.update()


def update_game_state():
    # Updates aliens and bullet movement in the same loops
    select_alien()
    move_aliens_right()
    move_aliens_down()
    move_aliens_right()
    move_aliens_down()
    move_aliens_left()
    move_aliens_down()
    move_aliens_left()
    move_aliens_down()


root = Screen()
root.title("Space Invaders")
root.setup(width=800, height=800)
root.bgcolor("black")
root.tracer(0)

scoreboard = Scoreboard()
ship = Ship()
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
