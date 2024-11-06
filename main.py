from src.Engine import Engine
from src.UI import Alignment
from src.UI.UILevel import UILevel
from src.UI.UIText import UIText


engine = Engine()
menu = UILevel()
menu.size_x = 100
text = UIText()
text.setText("Hello World")
text.setSizeX(20)
text.setSizeY(3)
menu.addObject(text)

engine.setCurrentLevel(menu)
engine.display()