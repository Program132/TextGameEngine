from src.Engine import Engine
from src.Level import Level
import keyboard
import time
from src.Models.Point import Point

engine = Engine(50, 5, ".")
mainLevel = Level(engine)

PLAYER_POINT = Point(3, 1)

mainLevel.addObject(PLAYER_POINT)
engine.setCurrentLevel(mainLevel)
engine.display()

running = True
while running:
    if keyboard.is_pressed("esc"):
        running = False

    time.sleep(0.001)
