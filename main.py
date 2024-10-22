import time
import keyboard
from src.Engine import Engine
from src.Level import Level
from src.Player import Player

engine = Engine(50, 5, ".")
mainLevel = Level(engine)

PLAYER = Player(3, 1, 'P')

mainLevel.addObject(PLAYER)
engine.setCurrentLevel(mainLevel)
engine.display()

def manageKeysPressed(event):
    if event.name == "w" or event.name == "z":
        mainLevel.removeObject(PLAYER.getX(), PLAYER.getY())
        PLAYER.setY(PLAYER.getY() - 1)
        mainLevel.addObject(PLAYER)
        engine.refresh()
    elif event.name == "s":
        mainLevel.removeObject(PLAYER.getX(), PLAYER.getY())
        PLAYER.setY(PLAYER.getY() + 1)
        mainLevel.addObject(PLAYER)
        engine.refresh()


keyboard.on_press(manageKeysPressed)

running = True
while running:
    if keyboard.is_pressed("esc"):
        running = False

    time.sleep(0.001)