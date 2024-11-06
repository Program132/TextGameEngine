from src.UI.UIText import UIText


class UILevel:
    def __init__(self, x:int = 20, y:int = 7):
        self.points_map = {}
        self.size_x = x
        self.size_y = y
        self.objects = []
        self.backgroundChar = "."

    def getSizeX(self):
        return self.size_x

    def setSizeX(self, x: int):
        self.size_x = x

    def getSizeY(self):
        return self.size_y

    def setSizeY(self, y: int):
        self.size_y = y

    def getPointsMap(self):
        return self.points_map

    def setPointsMap(self, points_map: dict):
        self.points_map = points_map

    def getObjects(self):
        return self.objects

    def setObjects(self, objects: list):
        self.objects = objects

    def getBackgroundChar(self):
        return self.backgroundChar

    def setBackgroundChar(self, char: str):
        self.backgroundChar = char

    def addObject(self, obj):
        self.objects.append(obj)

    def removeObject(self, obj):
        self.objects.remove(obj)

    def removeAllObjects(self):
        self.objects = []

    def display(self):
        self.points_map = {}
        s = ""

        for obj in self.objects:
            if isinstance(obj, UIText):
                for p in obj.getPoints():
                    self.points_map[(p.getX(), p.getY())] = p

        for y in range(self.size_y + 1):
            for x in range(self.size_x + 1):
                if (x, y) in self.points_map and self.points_map[(x, y)] is not None:
                    s += self.points_map[(x, y)].getChar()
                else:
                    s += self.backgroundChar
            s += "\n"
        print(s)

    def getPoint(self, x: int, y: int):
        if (x, y) in self.points_map:
            return self.points_map[(x, y)]
        return None