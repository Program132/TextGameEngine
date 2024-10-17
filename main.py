from src.Engine import Engine
from src.Level import Level
from src.Segment import Segment
from src.Triangle import Triangle

engine = Engine(50, 5, ".")

mainLevel = Level(engine)

mainLevel.addObject(Triangle(Segment(10, 4, 12, 4), 11, 3))
mainLevel.addObject(Triangle(Segment(20, 3, 22, 3), 21, 4))

engine.setCurrentLevel(mainLevel)
engine.display()
