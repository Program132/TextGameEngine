from src.Point import Point
from src.Segment import Segment
from src.Rectangle import Rectangle

class Engine:
    def __init__(self, x=20, y=8, c='.'):
        self.size_x = x
        self.size_y = y
        self.objects = []
        self.char = c

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

        for y in range(0, self.size_y + 1):
            for x in range(0, self.size_x + 1):
                if (x, y) in points_map:
                    s += points_map[(x, y)]
                else:
                    s += self.char
            s += "\n"
        print(s)

    def addObject(self, o):
        self.objects.append(o)

    def removeObject(self, x: int, y: int):
        for i in range(0, len(self.objects)):
            o = self.objects[i]
            if isinstance(o, Point) and o.getX() == x and o.getY() == y:
                del self.objects[i]

    def refresh(self):
        print("\n" * 100)
        self.display()
