from src.Objects.Object import Object
import math

class Ellipse(Object):
    def __init__(self, x: int, y: int, width: int, height: int, char: str = "-", fill: bool = True):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.char = char
        self.color = (255, 255, 255)
        self.fill = fill
        self._generatePoints()

    def _generatePoints(self):
        self.points = []
        rx = self.width / 2
        ry = self.height / 2
        cx = self.x + rx
        cy = self.y + ry
        for iy in range(self.y, self.y + self.height):
            for ix in range(self.x, self.x + self.width):
                if rx == 0 or ry == 0:
                    continue
                ellipse_eq = ((ix - cx) ** 2) / (rx ** 2) + ((iy - cy) ** 2) / (ry ** 2)
                if self.fill:
                    if ellipse_eq <= 1:
                        self.points.append((ix, iy, (self.char, self.color)))
                else:
                    if 0.9 <= ellipse_eq <= 1.1:
                        self.points.append((ix, iy, (self.char, self.color)))

    def setColorCharacter(self, rgb: tuple):
        self.color = rgb
        self._generatePoints()

    def setDisplayCharacter(self, c: str):
        self.char = c
        self._generatePoints()

    def getPoints(self):
        return self.points
