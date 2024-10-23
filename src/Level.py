from src.Engine import Engine
from src.Models.Point import Point
from src.Models.Segment import Segment
from src.Models.Triangle import Triangle
from src.Models.Rectangle import Rectangle
from src.Models.Circle import Circle
from src.Player import Player
from src.UI.Score import Score


class Level:
    def __init__(self, e: Engine = None):
        self.objects = []
        self.engine = e
        self.points_map = {}
        self.score = None

    def addObject(self, o):
        self.objects.append(o)

    def removeObject(self, x: int, y: int):
        if (x, y) in self.points_map:
            del self.points_map[(x, y)]

        for i in range(len(self.objects)):
            o = self.objects[i]

            if isinstance(o, Point) and o.getX() == x and o.getY() == y:
                del self.objects[i]
                break

            elif isinstance(o, Segment):
                for point in o.getPoints():
                    if point.getX() == x and point.getY() == y:
                        del self.objects[i]
                        break

            elif isinstance(o, Rectangle):
                for point in o.getPoints():
                    if point.getX() == x and point.getY() == y:
                        del self.objects[i]
                        break

            elif isinstance(o, Triangle):
                for point in o.getPoints():
                    if point.getX() == x and point.getY() == y:
                        del self.objects[i]
                        break

            elif isinstance(o, Circle):
                for point in o.getPoints():
                    if point.getX() == x and point.getY() == y:
                        del self.objects[i]
                        break

            elif isinstance(o, Player) and o.getX() == x and o.getY() == y:
                del self.objects[i]
                break

    def display(self):
        self.points_map = {}
        s = ""

        for obj in self.objects:
            if isinstance(obj, Score):
                content = ""
                if obj.showTitle():
                    content += obj.getTitle()
                for sName, sValue in obj.getScores().items():
                    if obj.showPredecessorScore():
                        content += f"{obj.getPredecessorScore()}{sName} : {sValue}\n"
                    else:
                        content += f"{sName} : {sValue}\n"
                print(content)
            elif isinstance(obj, Point):
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
            elif isinstance(obj, Player):
                self.points_map[(obj.getX(), obj.getY())] = obj.getChar()

        for y in range(self.engine.getSizeY() + 1):
            for x in range(self.engine.getSizeX() + 1):
                if (x, y) in self.points_map and self.points_map[(x, y)] is not None:
                    s += self.points_map[(x, y)]
                else:
                    s += self.engine.getChar()
            s += "\n"
        print(s)

    def getPoint(self, x: int, y: int):
        if (x, y) in self.points_map:
            return self.points_map[(x, y)]
        return None

    def getLevelScore(self):
        return self.score

    def removeLevelScore(self):
        self.score = None

    def updateLevelScore(self, s: Score):
        self.score = s
