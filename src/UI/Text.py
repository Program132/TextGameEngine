from .UIObject import UIObject

class Text(UIObject):
    def __init__(self, text="", x=0, y=0, color=(255, 255, 255),
                 align_x=UIObject.Alignment.LEFT, align_y=UIObject.Alignment.TOP):
        super().__init__(x, y, align_x, align_y)
        self.text = text
        self.color = color

    def set_text(self, text):
        self.text = text

    def set_color(self, color):
        self.color = color

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        if not self.visible:
            return
        r, g, b = self.color
        width = len(self.text)
        height = 1
        self.compute_position(self.term_cols, self.term_rows, width, height)
        print(f"\033[{int(self.computed_y)};{int(self.computed_x)}H"
              f"\033[38;2;{r};{g};{b}m{self.text}\033[0m")
        