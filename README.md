# Text Game Engine

Text Game Engine is a project in Python to create 2D games with a text style, like in a terminal.

# Example

```python
from src.Engine import Engine
from src.Level import Level
from src.Point import Point
from src.Rectangle import Rectangle
from src.Segment import Segment

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
from src.Segment import Segment
from src.Triangle import Triangle

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

# Documentation

[Engine](doc/Engine.md): The Engine class, the main one, managing the game.

[Level](doc/Level.md): The Level class, managing the different "place", locations, levels.

[Point](doc/Point.md): The Point class.

[Segment](doc/Segment.md): The Segment class.

[Rectangle](doc/Rectangle.md): The Rectangle class.

[Circle](doc/Circle.md): The Circle class.