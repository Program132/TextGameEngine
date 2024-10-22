from src.Models.Segment import Segment


class Rectangle:
    def __init__(self, up_x: int = 0, up_y: int = 0, down_x: int = 1, down_y: int = 1, collide: bool = False):
        self.up_x = up_x
        self.up_y = up_y
        self.down_x = down_x
        self.down_y = down_y
        self.canCollide = collide

    def getUpX(self):
        return self.up_x

    def getUpY(self):
        return self.up_y

    def getDownX(self):
        return self.down_x

    def getDownY(self):
        return self.down_y

    def getCanCollide(self):
        return self.canCollide

    def setUpX(self, x: int):
        self.up_x = x

    def setUpY(self, y: int):
        self.up_y = y

    def setDownX(self, x: int):
        self.down_x = x

    def setDownY(self, y: int):
        self.down_y = y

    def setCanCollide(self, c: bool):
        self.canCollide = c

    def getSegments(self):
        return [
            # up, down, left, right
            Segment(self.up_x, self.up_y, self.down_x, self.up_y, self.canCollide, "-"),
            Segment(self.up_x, self.down_y, self.down_x, self.down_y, self.canCollide, "-"),
            Segment(self.up_x, self.up_y + 1, self.up_x, self.down_y - 1, self.canCollide, "|"),
            Segment(self.down_x, self.up_y + 1, self.down_x, self.down_y - 1, self.canCollide, "|")
        ]

    def getPoints(self):
        l = []
        segments = self.getSegments()
        for s in segments:
            l.extend(s.getPoints())
        return l
