from src.Engine import Engine
from src.Models.Point import Point
from src.Models.Segment import Segment
from src.Models.Triangle import Triangle
from src.Models.Rectangle import Rectangle
from src.Models.Circle import Circle


class Level:
    def __init__(self, e: Engine = None):
        self.objects = []
        self.engine = e
        self.points_map = {}

    def addObject(self, o):
        self.objects.append(o)

    def removeObject(self, x: int, y: int):
        # Supprimer la position correspondante dans points_map
        if (x, y) in self.points_map:
            del self.points_map[(x, y)]

        # Supprimer l'objet de la liste
        for i in range(len(self.objects)):
            o = self.objects[i]
            if isinstance(o, Point) and o.getX() == x and o.getY() == y:
                del self.objects[i]
                break

    def display(self):
        self.points_map = {}  # Réinitialise la carte des points à chaque affichage
        s = ""

        for obj in self.objects:
            if isinstance(obj, Point):
                self.points_map[(obj.getX(), obj.getY())] = obj.getChar()
            elif isinstance(obj, Segment):
                for point in obj.getPoints():
                    self.points_map[(point.getX(), point.getY())] = point.getChar()
            elif isinstance(obj, Rectangle):
                for point in obj.getPoints():
                    self.points_map[(point.getX(), point.getY())] = point.getChar()
            elif isinstance(obj, Triangle):
                for point in obj.getPoints():
                    self.points_map[(point.getX(), point.getY())] = point.getChar()
            elif isinstance(obj, Circle):
                for point in obj.getPoints():
                    self.points_map[(point.getX(), point.getY())] = point.getChar()

        for y in range(self.engine.getSizeY() + 1):
            for x in range(self.engine.getSizeX() + 1):
                if (x, y) in self.points_map and self.points_map[(x, y)] is not None:
                    s += self.points_map[(x, y)]
                else:
                    s += self.engine.getChar()
            s += "\n"
        print(s)
