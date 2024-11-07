import time

from src.Engine import Engine
from src.UI.UILevel import UILevel
from src.UI.UIButton import UIButton
from src.Sounds.Sounds import Sounds

engine = Engine()
menu = UILevel()
menu.size_x = 100

s = Sounds("/home/User/Desktop/note.wav")

def my_button_action():
    print("Button 'clicked' action done")
    s.play()

button = UIButton(x=5, y=3, sx=15, sy=3, key='a')
button.setOnClick(my_button_action)

menu.addObject(button)
engine.setCurrentLevel(menu)
engine.display()

while True:
    button.listenForClick()

    time.sleep(0.1)