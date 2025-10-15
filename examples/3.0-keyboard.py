from src.Keyboard import Keyboard
from src.Enums.Keys import Keys
import time

def move_left():
    print("← Left pressed")

def move_up():
    print("↑ Up pressed")

kb = Keyboard()
kb.bind(Keys.LEFT, move_left)
kb.bind(Keys.UP, move_up)

while True:
    time.sleep(0.1)