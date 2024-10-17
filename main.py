from src.Engine import Engine
from src.Level import Level
from src.Point import Point
from src.Segment import Segment
from src.Triangle import Triangle

engine = Engine(50, 5, ".")

mainLevel = Level(engine)

mainLevel.addObject(Point(0, 0, "*"))
mainLevel.addObject(Triangle(Segment(1,1,3,1), 1,0))

engine.setCurrentLevel(mainLevel)
engine.display()