# Text Game Engine

Text Game Engine is a project in Python to create 2D games with a text style, like in a terminal.

# Example

```python
from src.Engine import Engine
from src.Level import Level
from src.Models.Point import Point
from src.Models.Rectangle import Rectangle
from src.Models.Segment import Segment

engine = Engine(50, 5, ".")
mainLevel = Level(engine)
mainLevel.addObject(Point(0, 0, "*"))
mainLevel.addObject(Point(50, 0, "*"))
mainLevel.addObject(Point(50, 5, "*"))
mainLevel.addObject(Segment(5, 2, 15, 2))
mainLevel.addObject(Segment(10, 3, 10, 6, False, "|"))
mainLevel.addObject(Segment(18, 3, 23, 4))
mainLevel.addObject(Rectangle(30, 3, 35, 5))
engine.setCurrentLevel(mainLevel)
engine.display()
```
```
*.................................................*
...................................................
.....-----------...................................
..........|.......---.........------...............
..........|..........---......|....|...............
..........|...................------..............*
```

Draw a Christmas tree:

```python
from src.Engine import Engine
from src.Level import Level
from src.Models.Segment import Segment
from src.Models.Triangle import Triangle

engine = Engine(50, 5, ".")
mainLevel = Level(engine)
up = Triangle(Segment(1, 2, 5, 2), 3, 0)
up.setUpPointChar("*")
mainLevel.addObject(up)
mainLevel.addObject(Segment(3, 4, 3, 3, False, "|"))
engine.setCurrentLevel(mainLevel)
engine.display()
```
```
...*...............................................
../.\..............................................
./___\.............................................
...|...............................................
...|...............................................
...................................................
```

Example with a player that can move in the current map and
cannot have collision with here a point, but it can be a segment, a rectangle and other, in itself all the points which have the collision activated. 
```python 
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
```

# Documentation

[Engine](doc/Engine.md): The Engine class, the main one, managing the game.

[Level](doc/Level.md): The Level class, managing the different "place", locations, levels.

[Point](doc/Point.md): The Point class.

[Segment](doc/Segment.md): The Segment class.

[Rectangle](doc/Rectangle.md): The Rectangle class.

[Circle](doc/Circle.md): The Circle class.

[Inputs](doc/Circle.md): Manage inputs from user.

[Player](doc/Circle.md): Player class, your main character in your game.