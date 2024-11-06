# Description

The snake game without the tale's snake

# Code

```python
import time
import random
import keyboard

from src.Engine import Engine
from src.Level import Level
from src.Models.Point import Point
from src.UI.Score import Score, Alignment

SIZE_X = 20
SIZE_Y = 10

engine = Engine(SIZE_X, SIZE_Y)
level = Level(engine)

snake = Point(5, 3)
snake.addTag("snake")
snake.setChar("S")
snake.setCanCollide(False)

score = Score()
score.addScore("Size Snake", 1)
score.setAlignment(Alignment.CENTER)


def spawnFruit():
    x = random.randint(2, SIZE_X)
    y = random.randint(2, SIZE_Y)
    p = Point(x, y)
    p.setChar("*")
    p.setCanCollide(False)
    p.addTag("fruit")
    return p


direction = "down"


def keyPressed(event):
    global direction
    if event.name == "bas" or event.name == "down":
        direction = "down"
    elif event.name == "haut" or event.name == "up":
        direction = "up"
    elif event.name == "gauche" or event.name == "left":
        direction = "left"
    elif event.name == "droite" or event.name == "right":
        direction = "right"


keyboard.on_press(keyPressed)

level.addObject(snake)
level.addObject(score)
fruit = spawnFruit()
level.addObject(fruit)

engine.setCurrentLevel(level)
engine.display()

running = True
while running:
    if (snake.getY() < 0 or snake.getY() > SIZE_Y) or (snake.getX() < 0 or snake.getX() > SIZE_X):
        print("Game Over")
        print("Score: " + str(score.getScore("Size Snake")))
        exit(1)

    level.removeObject(snake.getX(), snake.getY())
    if direction == "down":
        snake.setY(snake.getY() + 1)
    elif direction == "up":
        snake.setY(snake.getY() - 1)
    elif direction == "left":
        snake.setX(snake.getX() - 1)
    elif direction == "right":
        snake.setX(snake.getX() + 1)
    level.addObject(snake)

    # check if fruit at current XY:
    currentPoint = level.getPoint(snake.getX(), snake.getY())
    if currentPoint is not None and isinstance(currentPoint, Point) and currentPoint.hasTag("fruit"):
        score.updateScore("Size Snake", score.getScore("Size Snake") + 1)
        level.updateLevelScore(score)
        level.removeObject(fruit.getX(), fruit.getY())
        fruit = spawnFruit()
        level.addObject(fruit)

    engine.refresh()

    if keyboard.is_pressed("esc"):
        running = False

    pause_time = 0.800 / (score.getScore("Size Snake"))
    time.sleep(pause_time)
```