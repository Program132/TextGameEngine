class Point:
    def __init__(self, x=0, y=0, c='*'):
        self.x = x
        self.y = y
        self.char = c

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getChar(self):
        return self.char

    def setX(self, x:int):
        self.x = x

    def setY(self, y:int):
        self.x = y

    def setChar(self, c:str):
        self.char = c