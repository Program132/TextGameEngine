from src.Engine import Engine
from src.Point import Point
from src.Rectangle import Rectangle
from src.Segment import Segment

engine = Engine(50, 5)

engine.addObject(Point(0, 0, "*"))
engine.addObject(Point(50, 0, "*"))
engine.addObject(Point(50, 5, "*"))

engine.addObject(Segment(5, 2, 15, 2))
engine.addObject(Segment(10, 3, 10, 6, False, "|"))
engine.addObject(Segment(20, 3, 21, 4))

engine.addObject(Rectangle(30, 3, 35, 5))

engine.display()
