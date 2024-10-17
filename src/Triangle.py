from src.Segment import Segment
from src.Point import Point


class Triangle:
    def __init__(self, seg: Segment = None, x_up:int=0, y_up:int=0):
        self.base = seg
        self.upPoint = Point(x_up, y_up)

    def getBase(self):
        return self.base

    def getUpPoint(self):
        return self.upPoint

    def setBase(self, base: Segment):
        self.base = base

    def setUpPoint(self, p: Point):
        self.upPoint = p

    def getPoints(self):
        points = []

        # Get points for the base of the triangle
        base_points = self.base.getPoints()
        points.extend(base_points)

        # Get the left and right points of the base
        x_left, y_left = self.base.getX1(), self.base.getY1()
        x_right, y_right = self.base.getX2(), self.base.getY2()

        # Get the top point of the triangle
        x_top, y_top = self.upPoint.getX(), self.upPoint.getY()

        # Create the left side segment (top to left base point)
        left_side = Segment(x_top, y_top, x_left, y_left, False, "\\")
        left_points = left_side.getPoints()
        points.extend(left_points)

        # Create the right side segment (top to right base point)
        right_side = Segment(x_top, y_top, x_right, y_right, False, "/")
        right_points = right_side.getPoints()
        points.extend(right_points)

        return points