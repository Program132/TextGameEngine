# Text Game Engine

Text Game Engine is a project in Python to create 2D games with a text style, like in a terminal.

# Example

```
from src.Engine import Engine
from src.Point import Point
from src.Segment import Segment

engine = Engine(50, 5)
engine.addObject(Point(0, 0, "*"))
engine.addObject(Point(50, 0, "*"))
engine.addObject(Point(50, 5, "*"))
engine.addObject(Segment(5, 2, 15, 2))
engine.addObject(Segment(10, 3, 10, 6, False, "|"))
engine.addObject(Segment(25, 3, 30, 4))
engine.display()
```
```
*.................................................*
...................................................
.....-----------...................................
..........|..............---.......................
..........|.................---....................
..........|.......................................*
```

# Documentation

[Engine](doc/Engine.md): The main class which contain objects, parameter for your game, etc.

[Point](doc/Point.md): The Point class.

[Segment](doc/Segment.md): The Segment class.