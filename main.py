from turtle import Screen
from tkinter import font
from ship import Ship
from scoreboard import Scoreboard
from bullet import Bullet
from aliens import Aliens

root = Screen()
root.title("Space Invaders")
root.setup(width=800, height=800)
root.bgcolor("black")
root.tracer(0)

ship = Ship()
scoreboard = Scoreboard()
bullet = Bullet()
alien = Aliens()

root.update()
root.mainloop()
