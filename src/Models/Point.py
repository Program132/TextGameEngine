class Point:
    def __init__(self, x=0, y=0, c='*'):
        self.x = x
        self.y = y
        self.char = c
        self.canCollide = False
        self.tags = []

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getChar(self):
        return self.char

    def setX(self, x: int):
        self.x = x

    def setY(self, y: int):
        self.y = y

    def setChar(self, c: str):
        self.char = c

    def getCanCollide(self):
        return bool(self.canCollide)

    def setCanCollide(self, c: bool):
        self.canCollide = c

    def hasTag(self, name: str):
        for t in self.tags:
            if t == name:
                return True
        return False

    def addTag(self, name: str):
        self.tags.append(name)

    def removeTag(self, name: str):
        for i in range(len(self.tags)):
            if self.tags[i] == name:
                del self.tags[i]

    def __str__(self):
        return f"({self.getX()}, {self.getY()})"

    def __repr__(self):
        return f"({self.getX()}, {self.getY()})"