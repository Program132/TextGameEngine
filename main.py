from src.Engine import Engine
from src.Level import Level
import keyboard
import time
from src.Point import Point

engine = Engine(50, 5, ".")
mainLevel = Level(engine)

PLAYER_POINT = Point(3, 1)

mainLevel.addObject(PLAYER_POINT)
engine.setCurrentLevel(mainLevel)
engine.display()


def manageKeysPressed(event):
    if event.name == "z":
        mainLevel.removeObject(PLAYER_POINT.getX(), PLAYER_POINT.getY())
        PLAYER_POINT.setY(PLAYER_POINT.getY() - 1)
        mainLevel.addObject(PLAYER_POINT)
        engine.refresh()
    elif event.name == "s":
        mainLevel.removeObject(PLAYER_POINT.getX(), PLAYER_POINT.getY())
        PLAYER_POINT.setY(PLAYER_POINT.getY() + 1)
        mainLevel.addObject(PLAYER_POINT)
        engine.refresh()


keyboard.on_press(manageKeysPressed)

running = True
while running:
    if keyboard.is_pressed("esc"):
        running = False

    time.sleep(0.001)
