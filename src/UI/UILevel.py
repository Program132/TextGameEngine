from .UIObject import UIObject

class UILevel:
    def __init__(self):
        self.objects = []
        self.term_cols = 80
        self.term_rows = 24

    def addObject(self, obj: UIObject):
        self.objects.append(obj)
        obj.term_cols = self.term_cols
        obj.term_rows = self.term_rows

    def update(self, delta):
        for obj in self.objects:
            obj.update(delta)

    def display(self):
        print("\033[H\033[J", end="")
        for obj in self.objects:
            obj.display()
            