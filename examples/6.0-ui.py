from src.Engine import Engine
from src.UI.UILevel import UILevel
from src.UI.Text import Text
from src.UI.TextAsciiArt import TextAsciiArt
from src.UI.Button import Button
from src.UI.UIObject import UIObject
from src.Utils.TerminalWindow import TerminalWindow
import time
import threading
import random

def get_random_rgb():
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    return (r, g, b)

def main():
    term = TerminalWindow()
    TERM_WIDTH = term.getWidth()
    TERM_HEIGHT = term.getHeight()

    ui_level = UILevel()
    ui_level.term_cols = TERM_WIDTH
    ui_level.term_rows = TERM_HEIGHT

    def handle_button_click():
        new_color = get_random_rgb()
        button.set_color(new_color)

    title = TextAsciiArt(
        "TextGameEngine",
        font="slant",
        color=(0, 255, 255),
        x=0, y=2,
        align_x=UIObject.Alignment.CENTER,
        align_y=UIObject.Alignment.TOP
    )

    button = Button(
        "Start",
        on_click=handle_button_click,
        x=0, y=TERM_HEIGHT//2,
        align_x=UIObject.Alignment.CENTER,
        align_y=UIObject.Alignment.TOP,
        color=(255, 255, 255)
    )

    ui_level.addObject(title)
    ui_level.addObject(button)

    engine = Engine(fps=10)
    engine.setLevel(ui_level)

    try:
        engine.start()
    except KeyboardInterrupt:
        print("\n[Engine stopped]")

if __name__ == "__main__":
    main()