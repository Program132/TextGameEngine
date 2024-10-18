from src.Cercle import Cercle
from src.Engine import Engine
from src.Level import Level

engine = Engine(50, 5, ".")

mainLevel = Level(engine)

mainLevel.addObject(Cercle(10, 3, 2))

engine.setCurrentLevel(mainLevel)
engine.display()
