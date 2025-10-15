from src.Objects.Object import Object

class Rectangle(Object):
    def __init__(self, x: int, y: int, width: int, height: int, char: str = "*", fill: bool = True):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.char = char
        self.color = (255, 255, 255)
        self.fill = fill
        self._generatePoints()

    def _generatePoints(self):
        self.points = []
        for dy in range(self.height):
            for dx in range(self.width):
                if self.fill:
                    self.points.append((self.x + dx, self.y + dy, (self.char, self.color)))
                else:
                    if dy == 0 or dy == self.height - 1 or dx == 0 or dx == self.width - 1:
                        self.points.append((self.x + dx, self.y + dy, (self.char, self.color)))

    def setColorCharacter(self, rgb: tuple):
        self.color = rgb
        self._generatePoints()

    def setDisplayCharacter(self, c: str):
        self.char = c
        self._generatePoints()