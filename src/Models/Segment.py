from src.Models.Point import Point


class Segment:
    def __init__(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0, collide: bool = False, c: str = "-"):
        self.left_x = x1
        self.left_y = y1
        self.right_x = x2
        self.right_y = y2
        self.canCollide = False  # Collision
        self.char = c

    def getX1(self):
        return self.left_x

    def getY1(self):
        return self.left_y

    def getX2(self):
        return self.right_x

    def getY2(self):
        return self.right_y

    def getCanCollide(self):
        return self.canCollide

    def getChar(self):
        return self.char

    def setX1(self, x: int):
        self.left_x = x

    def setY1(self, y: int):
        self.left_y = y

    def setX2(self, x: int):
        self.right_x = x

    def setY2(self, y: int):
        self.right_y = y

    def setCanCollide(self, canCollide: bool):
        self.canCollide = canCollide

    def setChar(self, char):
        self.char = char

    def getPoints(self):
        l = []
        x1, y1 = self.left_x, self.left_y
        x2, y2 = self.right_x, self.right_y

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            l.append(Point(x1, y1, self.char))
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

        return l

