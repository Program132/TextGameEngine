from .UIObject import UIObject
from src.Utils.TerminalWindow import TerminalWindow
from src.Utils.MouseTracker import MouseTracker

class Button(UIObject):
    def __init__(self, text="", on_click=None, x=0, y=0,
                 align_x=UIObject.Alignment.LEFT, align_y=UIObject.Alignment.TOP,
                 color=(255,255,255), bg_color=(50,50,50)):
        super().__init__(x, y, align_x, align_y)
        self.text = text
        self.on_click = on_click
        self.color = color
        self.bg_color = bg_color

        self.width = len(self.text) + 4
        self.height = 3

        self.on_left_click_func = on_click
        self.term = TerminalWindow()
        self.tracker = MouseTracker(self.term)
        self.tracker.on_left_click(self.on_left_click)
        self.tracker.start()

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_text(self, text):
        self.text = text
        self.width = len(self.text) + 4

    def set_color(self, color):
        self.color = color

    def set_bg_color(self, color):
        self.bg_color = color

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        if not self.visible:
            return

        self.compute_position(self.term_cols, self.term_rows, self.width, self.height)

        x = int(self.computed_x)
        y = int(self.computed_y)
        r, g, b = self.color
        br, bg, bb = self.bg_color

        print(f"\033[{y};{x}H\033[48;2;{br};{bg};{bb}m+{'-'*(self.width-2)}+\033[0m")
        print(f"\033[{y+1};{x}H\033[48;2;{br};{bg};{bb}m| \033[38;2;{r};{g};{b}m{self.text}\033[48;2;{br};{bg};{bb}m |\033[0m")
        print(f"\033[{y+2};{x}H\033[48;2;{br};{bg};{bb}m+{'-'*(self.width-2)}+\033[0m")

    def is_clicked(self, click_x: int, click_y: int) -> bool:
        if self.computed_x is None:
            return False

        start_x = self.computed_x-1
        start_y = self.computed_y-1
        end_x = self.computed_x + self.width
        end_y = self.computed_y + self.height

        is_inside_x = start_x <= click_x < end_x
        is_inside_y = start_y <= click_y < end_y

        return is_inside_x and is_inside_y

    def on_left_click(self, click_x: int, click_y: int):
        if self.is_clicked(click_x, click_y):
            if self.on_left_click_func is not None:
                self.on_left_click_func()

    def click(self):
        if self.on_click:
            self.on_click()