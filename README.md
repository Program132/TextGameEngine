# Text Game Engine

Text Game Engine is a project in Python to create 2D games with a text style, like in a terminal.

# Example

```
from src.Engine import Engine
from src.Level import Level
from src.Point import Point
from src.Rectangle import Rectangle
from src.Segment import Segment

engine = Engine(50, 5, ".")

mainLevel = Level(0, engine)

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

# Documentation

[Engine](doc/Engine.md): The Engine class, the main one, managing the game.

[Level](doc/Level.md): The Level class, managing the different "place", locations, levels.

[Point](doc/Point.md): The Point class.

[Segment](doc/Segment.md): The Segment class.

[Rectangle](doc/Rectangle.md): The Rectangle class.