import time
import keyboard
from src.Engine import Engine
from src.Level import Level
from src.Player import Player
from src.Models.Point import Point

engine = Engine(50, 5, ".")
mainLevel = Level(engine)

PLAYER = Player(3, 1, 'P')
wall_left = Point(5, 3)
wall_left.setCanCollide(True)

mainLevel.addObject(PLAYER)
mainLevel.addObject(wall_left)
engine.setCurrentLevel(mainLevel)
engine.display()


def manageKeysPressed(event):
    if event.name == "w" or event.name == "z":
        mainLevel.removeObject(PLAYER.getX(), PLAYER.getY())
        PLAYER.moveUp()
        currentPoint = mainLevel.getPoint(PLAYER.getX(), PLAYER.getY())
        if currentPoint is None or (isinstance(currentPoint, Point) and not currentPoint.canCollide()):
            mainLevel.addObject(PLAYER)
            engine.refresh()
        else:
            PLAYER.moveDown()
            mainLevel.addObject(PLAYER)
            engine.refresh()
    elif event.name == "s":
        mainLevel.removeObject(PLAYER.getX(), PLAYER.getY())
        PLAYER.moveDown()
        currentPoint = mainLevel.getPoint(PLAYER.getX(), PLAYER.getY())
        if currentPoint is None or (isinstance(currentPoint, Point) and not currentPoint.canCollide()):
            mainLevel.addObject(PLAYER)
            engine.refresh()
        else:
            PLAYER.moveUp()
            mainLevel.addObject(PLAYER)
            engine.refresh()
    elif event.name == "d":
        mainLevel.removeObject(PLAYER.getX(), PLAYER.getY())
        PLAYER.moveRight()
        currentPoint = mainLevel.getPoint(PLAYER.getX(), PLAYER.getY())
        if currentPoint is None or (isinstance(currentPoint, Point) and not currentPoint.canCollide()):
            mainLevel.addObject(PLAYER)
            engine.refresh()
        else:
            PLAYER.moveLeft()
            mainLevel.addObject(PLAYER)
            engine.refresh()
    elif event.name == "q" or event.name == "a":
        mainLevel.removeObject(PLAYER.getX(), PLAYER.getY())
        PLAYER.moveLeft()
        currentPoint = mainLevel.getPoint(PLAYER.getX(), PLAYER.getY())
        if currentPoint is None or (isinstance(currentPoint, Point) and not currentPoint.canCollide()):
            mainLevel.addObject(PLAYER)
            engine.refresh()
        else:
            PLAYER.moveRight()
            mainLevel.addObject(PLAYER)
            engine.refresh()


keyboard.on_press(manageKeysPressed)

running = True
while running:
    if keyboard.is_pressed("esc"):
        running = False

    time.sleep(0.001)
