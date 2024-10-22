class Point:
    def __init__(self, x=0, y=0, c='*'):
        self.x = x
        self.y = y
        self.char = c
        self.canCollide = False

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
        return self.canCollide

    def setCanCollide(self, c: bool):
        self.canCollide = c

    def __str__(self):
        return f"({self.getX()}, {self.getY()})"

    def __repr__(self):
        return f"({self.getX()}, {self.getY()})"