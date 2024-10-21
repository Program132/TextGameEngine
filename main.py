from src.Engine import Engine
from src.Level import Level

engine = Engine(50, 5, " ")

mainLevel = Level(engine)


engine.setCurrentLevel(mainLevel)

engine.display()
