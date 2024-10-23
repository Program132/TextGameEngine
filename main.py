import time
import keyboard
from src.Engine import Engine
from src.Level import Level
from src.Player import Player
from src.Models.Point import Point
from src.Score import Score

engine = Engine(50, 5, ".")
mainLevel = Level(engine)

PLAYER = Player(3, 5, 'P')

scores = Score()
scores.addScore("point", 0)  # create a special score for points gained by the player

mainLevel.addObject(scores)  # add score objet
mainLevel.addObject(PLAYER)


engine.setCurrentLevel(mainLevel)
engine.display()


def manageKeysPressed(event):
    if event.name == "space" or event.name == "espace":
        # Manage score

        scores.updateScore("point", scores.getScore("point") + 1)
        mainLevel.updateLevelScore(scores)

        # Animation when the player jump:
        for i in range(0, 2):
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
            time.sleep(0.35)
        for i in range(2, 0, -1):
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
            time.sleep(0.35)
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
