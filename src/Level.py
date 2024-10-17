from src.Point import Point
from src.Segment import Segment
from src.Rectangle import Rectangle
from src.Engine import Engine

class Level:
    def __init__(self, e: Engine = None):
        self.objects = []
        self.engine = e

    def addObject(self, o):
        self.objects.append(o)

    def removeObject(self, x: int, y: int):
        for i in range(0, len(self.objects)):
            o = self.objects[i]
            if isinstance(o, Point) and o.getX() == x and o.getY() == y:
                del self.objects[i]
            elif isinstance(o, Segment) and o.getX1() == x and o.getY1() == y:
                del self.objects[i]
            elif isinstance(o, Rectangle) and o.getUpX() == x and o.getUpY() == y:
                del self.objects[i]

    def display(self):
        s = ""
        points_map = {}

        for obj in self.objects:
            if isinstance(obj, Point):
                points_map[(obj.getX(), obj.getY())] = obj.getChar()
            elif isinstance(obj, Segment):
                for point in obj.getPoints():
                    points_map[(point.getX(), point.getY())] = point.getChar()
            elif isinstance(obj, Rectangle):
                for point in obj.getPoints():
                    points_map[(point.getX(), point.getY())] = point.getChar()

        for y in range(0, self.engine.getSizeY() + 1):
            for x in range(0, self.engine.getSizeX() + 1):
                if (x, y) in points_map:
                    s += points_map[(x, y)]
                else:
                    s += self.engine.getChar()
            s += "\n"
        print(s)