import time
import keyboard

from src.Engine import Engine
from src.Level import Level
from src.Models.Segment import Segment
from src.Player import Player
from src.Models.Point import Point
from src.UI.Score import Score

SIZE_X = 50
SIZE_Y = 5

engine = Engine(SIZE_X, SIZE_Y, ".")
mainLevel = Level(engine)

PLAYER = Player(0, 4, 'X')

scores = Score()
scores.addScore("point", 0)

floor = Segment(0, SIZE_Y, SIZE_X, SIZE_Y)
floor.setChar("¯")


def createStar(x, y):
    p = Point(x, y)
    p.setCanCollide(False)
    p.setChar("*")
    p.addTag("star")
    return p


star1 = createStar(5, 2)
star2 = createStar(15, 2)
star3 = createStar(40, 1)

mainLevel.addObject(PLAYER)
mainLevel.addObject(floor)
mainLevel.addObject(star1)
mainLevel.addObject(star2)
mainLevel.addObject(star3)
mainLevel.addObject(scores)

lastHoveredPoint = None

engine.setCurrentLevel(mainLevel)
engine.display()


def manageKeysPressed(event):
    if event.name == "space" or event.name == "espace":
        # Animation when the player jump:
        for i in range(0, 3):
            mainLevel.removeObject(PLAYER.getX(), PLAYER.getY())
            PLAYER.moveUp()
            currentPoint = mainLevel.getPoint(PLAYER.getX(), PLAYER.getY())
            if currentPoint is None or not currentPoint.getCanCollide():
                # can do the action

                if not currentPoint is None and currentPoint.hasTag("star"):
                    scores.updateScore("point", scores.getScore("point") + 1)
                    mainLevel.updateLevelScore(scores)

                mainLevel.addObject(PLAYER)
                engine.refresh()
            else: # can't do the action
                PLAYER.moveDown()
                mainLevel.addObject(PLAYER)
                engine.refresh()
            time.sleep(0.35)
        for i in range(3, 0, -1):
            mainLevel.removeObject(PLAYER.getX(), PLAYER.getY())
            PLAYER.moveDown()
            currentPoint = mainLevel.getPoint(PLAYER.getX(), PLAYER.getY())
            if currentPoint is None or not currentPoint.getCanCollide():
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
        if currentPoint is None or not currentPoint.getCanCollide():
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
        if currentPoint is None or not currentPoint.getCanCollide():
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
