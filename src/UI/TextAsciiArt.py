from .UIObject import UIObject
import pyfiglet

class TextAsciiArt(UIObject):
    def __init__(self, text="", font="standard", color=(255, 255, 255),
                 x=0, y=0, align_x=UIObject.Alignment.LEFT, align_y=UIObject.Alignment.TOP):
        super().__init__(x, y, align_x, align_y)
        self.text = text
        self.font = font
        self.color = color
        self.update_figlet()

    def set_text(self, text):
        self.text = text
        self.update_figlet()

    def set_color(self, color):
        self.color = color

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_font(self, font):
        self.font = font
        self.update_figlet()

    def update_figlet(self):
        self.figlet_text = pyfiglet.figlet_format(self.text, font=self.font)

    def display(self):
        if not self.visible:
            return
        r, g, b = self.color
        lines = self.figlet_text.splitlines()
        width = max(len(line) for line in lines)
        height = len(lines)
        self.compute_position(self.term_cols, self.term_rows, width, height)
        for i, line in enumerate(lines):
            print(f"\033[{int(self.computed_y + i)};{int(self.computed_x)}H"
                  f"\033[38;2;{r};{g};{b}m{line}\033[0m")
            