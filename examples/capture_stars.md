# Description

Game with a menu that allows you to play or quit, the goal is to capture the most stars that descend, the player must be below / touch to increase his score.

# Code 

```python
import random
import time
import threading
from src import Level, Player, Engine
from src.Inputs import Inputs
from src.Models import Segment, Point
from src.UI import UILevel, UIButton, Score


def playBTN_clicked():
    global inGame, inMenu
    if inMenu:
        level0.addObject(score)
        level0.addObject(PLAYER)
        level0.addObject(ground)

        engine.setCurrentLevel(level0)
        engine.refresh()

        inGame = True
        inMenu = False

        stars_active.set()

def returnToMenu():
    global inGame, inMenu, stars
    if inGame:
        stars = []
        level0.clear()

        engine.setCurrentLevel(menu)
        engine.refresh()

        stars_active.clear()

        inMenu = True
        inGame = False

def quitBTN_clicked():
    if inMenu:
        exit(1)


def moveLeft():
    if inGame:
        level0.removeObject(PLAYER.getX(), PLAYER.getY())
        PLAYER.setX(max(0, PLAYER.getX() - 1))
        level0.addObject(PLAYER)
        engine.setCurrentLevel(level0)
        engine.refresh()

def moveRight():
    if inGame:
        level0.removeObject(PLAYER.getX(), PLAYER.getY())
        PLAYER.setX(min(SIZE_X - 1, PLAYER.getX() + 1))
        level0.addObject(PLAYER)
        engine.setCurrentLevel(level0)
        engine.refresh()

def spawnStar():
    if inGame and len(stars) < 3:
        star = Point()
        star.setChar("*")
        star.setY(0)
        star.setX(random.randint(2, SIZE_X - 2))
        star.addTag("star")

        stars.append(star)
        level0.addObject(star)
        engine.setCurrentLevel(level0)
        engine.refresh()

def moveStars():
    global stars
    while True:
        stars_active.wait()
        if inGame and stars:
            new_stars = []
            for star in stars:
                old_x, old_y = star.getX(), star.getY()
                new_y = old_y + 1
                if ((old_x == PLAYER.getX() and old_y == PLAYER.getY()) or
                        (old_x == PLAYER.getX() and new_y == PLAYER.getY())):
                    score.updateScore("Points", score.getScore("Points") + 1)
                    level0.updateLevelScore(score)
                    level0.removeObject(old_x, old_y)
                else:
                    if new_y < SIZE_Y:
                        level0.removeObject(old_x, old_y)
                        star.setY(new_y)
                        level0.addObject(star)
                        new_stars.append(star)
                    else:
                        level0.removeObject(old_x, old_y)
            stars = new_stars
            engine.setCurrentLevel(level0)
            engine.refresh()
            time.sleep(1)

def spawnStarsPeriodically():
    while True:
        time.sleep(3)
        if inGame:
            spawnStar()

SIZE_X = 24
SIZE_Y = 7

engine = Engine(SIZE_X, SIZE_Y, " ")

menu = UILevel()
menu.size_x = SIZE_X
menu.size_y = SIZE_Y
menu.setBackgroundChar(" ")

level0 = Level(engine)

PLAYER = Player()
PLAYER.setChar("X")
PLAYER.setY(SIZE_Y - 1)
PLAYER.setX(0)

score = Score()
score.addScore(scoreName="Points", scoreDefaultValue=0)

ground = Segment(0, SIZE_Y, SIZE_X, SIZE_Y)
ground.setCanCollide(True)
ground.setChar('¯')

playBTN = UIButton(x=5, y=0, sx=15, sy=1, key='p')
playBTN.setText("Play (P)")
playBTN.setOnClick(playBTN_clicked)
quitBTN = UIButton(x=5, y=4, sx=15, sy=1, key='q')
quitBTN.setText("Quit (Q)")
quitBTN.setOnClick(quitBTN_clicked)

menu.addObject(playBTN)
menu.addObject(quitBTN)

engine.setCurrentLevel(menu)
engine.display()

inGame = False
inMenu = True
stars = []

stars_active = threading.Event()
threading.Thread(target=moveStars, daemon=True).start()
threading.Thread(target=spawnStarsPeriodically, daemon=True).start()

while True:
    playBTN.listenForClick()
    quitBTN.listenForClick()

    Inputs("left", moveLeft).listenForInput()
    Inputs("right", moveRight).listenForInput()
    Inputs("gauche", moveLeft).listenForInput()
    Inputs("droite", moveRight).listenForInput()

    Inputs("esc", returnToMenu).listenForInput()

    time.sleep(0.01)

```