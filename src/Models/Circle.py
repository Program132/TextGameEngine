import math
from src.Models.Point import Point

class Circle:
    def __init__(self, x: int = 0, y: int = 0, r: int = 1):
        self.center_x = x
        self.center_y = y
        self.rayon = r
        self.UpChar = "_"
        self.LeftRightChar = "|"
        self.DownChar = "¯"
        self.VoidChar = ""

    def getCenterX(self):
        return self.center_x

    def getCenterY(self):
        return self.center_y

    def getRayon(self):
        return self.rayon

    def getUpChar(self):
        return self.UpChar

    def getLeftRightChar(self):
        return self.LeftRightChar

    def getDownChar(self):
        return self.DownChar

    def getVoidChar(self):
        return self.VoidChar

    def setCenterX(self, x: int):
        self.center_x = x

    def setCenterY(self, y: int):
        self.center_y = y

    def setRayon(self, r: int):
        self.rayon = r

    def setUpChar(self, char: str):
        self.UpChar = char

    def setLeftRightChar(self, char: str):
        self.LeftRightChar = char

    def setDownChar(self, char: str):
        self.DownChar = char

    def setVoidChar(self, char: str):
        self.VoidChar = char

    def getPoints(self):
        points = []

        up_point = Point(self.center_x, self.center_y - self.rayon, self.UpChar)
        points.append(up_point)

        left_point = Point(self.center_x - self.rayon, self.center_y, self.LeftRightChar)
        points.append(left_point)

        right_point = Point(self.center_x + self.rayon, self.center_y, self.LeftRightChar)
        points.append(right_point)

        down_point = Point(self.center_x, self.center_y + self.rayon, self.DownChar)
        points.append(down_point)

        for angle in range(0, 360):
            rad = math.radians(angle)
            x = self.center_x + int(self.rayon * math.cos(rad))
            y = self.center_y + int(self.rayon * math.sin(rad))

            if (x, y) not in [(up_point.getX(), up_point.getY()),
                              (left_point.getX(), left_point.getY()),
                              (right_point.getX(), right_point.getY()),
                              (down_point.getX(), down_point.getY())]:
                points.append(Point(x, y, " "))

        return points
