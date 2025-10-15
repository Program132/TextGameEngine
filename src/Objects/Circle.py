from src.Objects.Object import Object
import math

class Circle(Object):
    def __init__(self, x: int, y: int, radius: int, char: str = "O", fill: bool = True):
        super().__init__(x, y)
        self.radius = radius
        self.char = char
        self.color = (255, 255, 255)
        self.fill = fill
        self._generatePoints()

    def _generatePoints(self):
        self.points = []
        cx = self.x
        cy = self.y
        r = self.radius
        for iy in range(cy - r, cy + r + 1):
            for ix in range(cx - r, cx + r + 1):
                dx = ix - cx
                dy = iy - cy
                distance = math.sqrt(dx*dx + dy*dy)
                if self.fill:
                    if distance <= r:
                        self.points.append((ix, iy, (self.char, self.color)))
                else:
                    if r - 0.5 <= distance <= r + 0.5:
                        self.points.append((ix, iy, (self.char, self.color)))

    def setColorCharacter(self, rgb: tuple):
        self.color = rgb
        self._generatePoints()

    def setDisplayCharacter(self, c: str):
        self.char = c
        self._generatePoints()

    def getPoints(self):
        return self.points
