from src.Objects.Object import Object

class Point(Object):
    def __init__(self, x: int, y: int, char: str = "*"):
        super().__init__(x, y)
        self.char = char
        self.color = (255, 255, 255)
        self.points.append((x, y, (self.char, self.color)))

    def setColorCharacter(self, rgb: tuple):
        self.color = rgb
        self.points = [(self.x, self.y, (self.char, self.color))]

    def setDisplayCharacter(self, c: str):
        self.char = c
        self.points = [(self.x, self.y, (self.char, self.color))]
