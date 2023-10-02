import time
from turtle import Screen
from ship import Ship
from scoreboard import Scoreboard
from aliens import AlienManager, Alien

sleep_time = 0.03


def check_shoot_state(alien=Alien):
    if alien.is_shooting:
        alien.shooting()
    if ship.is_shooting:
        ship.shooting()


def check_hit_state(alien=Alien):
    try:
        if alien.bullet.hit_ship(ship):
            alien.bullet.hideturtle()
            del alien.bullet
            ship.lose_life()
            alien.can_shoot = True
            alien.is_shooting = False
    except AttributeError:
        pass
    try:
        if ship.bullet.hit_alien(alien):
            ship.bullet.hideturtle()
            del ship.bullet
            aliens.die(alien)
            ship.can_shoot = True
            ship.is_shooting = False
            scoreboard.score += 75
            scoreboard.update_scoreboard()
    except AttributeError:
        pass
    if alien.hit_ship(ship=ship):
        aliens.die(alien)
        ship.lose_life()


def move_aliens_down():
    for alien in aliens.swarm:
        if not ship.lives:
            break
        if aliens.reached_end():
            break
        alien.move_down()
        check_shoot_state(alien)
        check_hit_state(alien)
        root.update()


def move_aliens_right():
    for alien in aliens.swarm:
        if not ship.lives:
            break
        if aliens.reached_end():
            break
        alien.move_right()
        check_shoot_state(alien)
        check_hit_state(alien)
        root.update()


def move_aliens_left():
    for alien in aliens.swarm:
        if not ship.lives:
            break
        if aliens.reached_end():
            break
        alien.move_left()
        check_shoot_state(alien)
        check_hit_state(alien)
        root.update()


def update_game_state():
    if len(aliens.swarm) > 8:
        aliens.select_shooter()
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
    # Check for number of ship lives. If none remain, ship game state update and end game.
    if not ship.lives:
        playing = False
        scoreboard.game_over()
    # Check if aliens have reached the bottom of the screen. If so, end game.
    if aliens.reached_end():
        playing = False
        scoreboard.game_over()
    if not aliens.swarm:
        aliens.respawn()
        scoreboard.stage += 1
        sleep_time -= 0.005
    # Update game state. Skipped if no lives remain.
    if playing:
        root.update()
        update_game_state()
        time.sleep(sleep_time)

root.mainloop()
