from src.Models.Segment import Segment
from src.Models.Point import Point


class Triangle:
    def __init__(self, seg: Segment = None, x_up: int = 0, y_up: int = 0, collide: bool = False):
        self.base = seg
        self.upPoint = Point(x_up, y_up)
        self.upPointChar = "Ʌ"
        self.upPointCharInverted = "V"
        self.canCollide = collide

    def getBase(self):
        return self.base

    def getUpPoint(self):
        return self.upPoint

    def getUpPointChar(self):
        return self.upPointChar

    def getUpPointCharInverted(self):
        return self.upPointCharInverted

    def getCanCollide(self):
        return self.canCollide

    def setBase(self, base: Segment):
        self.base = base

    def setUpPoint(self, p: Point):
        self.upPoint = p

    def setUpPointChar(self, c: str):
        self.upPointChar = c

    def setUpPointCharInverted(self, c: str):
        self.upPointCharInverted = c

    def setCanCollide(self, c: bool):
        self.canCollide = c

    def getPoints(self):
        points = []

        base_segment = Segment(self.base.getX1(), self.base.getY1(), self.base.getX2(), self.base.getY2(), False, "_")

        x_left, y_left = self.base.getX1(), self.base.getY1()
        x_right, y_right = self.base.getX2(), self.base.getY2()

        if self.upPoint.getY() < y_left:  # up point is above base
            left_side = Segment(self.upPoint.getX(), self.upPoint.getY(), x_left, y_left, False, "/")
            left_points = left_side.getPoints()

            self.upPoint.setChar(self.getUpPointChar())

            right_side = Segment(self.upPoint.getX(), self.upPoint.getY(), x_right, y_right, False, "\\")
            right_points = right_side.getPoints()
        else:  # up point is under base
            left_side = Segment(self.upPoint.getX(), self.upPoint.getY(), x_left, y_left, False, "\\")
            left_points = left_side.getPoints()

            base_segment.setChar("¯")
            self.upPoint.setChar(self.getUpPointCharInverted())

            right_side = Segment(self.upPoint.getX(), self.upPoint.getY(), x_right, y_right, False, "/")
            right_points = right_side.getPoints()

        left_points = [p for p in left_points if p.getX() != self.upPoint.getX() or p.getY() != self.upPoint.getY()]
        right_points = [p for p in right_points if p.getX() != self.upPoint.getX() or p.getY() != self.upPoint.getY()]

        # Add all points to list
        points.append(self.upPoint)
        base_points = base_segment.getPoints()
        points.extend(base_points)
        points.extend(left_points)
        points.extend(right_points)

        for p in points:
            p.setCanCollide(self.canCollide)

        return points
