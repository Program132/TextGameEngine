from src.Textures.Pixel import Pixel

class Texture:
    def __init__(self, width: int, height: int):
        self.pixels = []
        self.width = width
        self.height = height
        self.__generateDefaultPixels()

    def __generateDefaultPixels(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                p = Pixel(x,y,"(255,255,255)")
                self.pixels.append(p)

    def setPixelColor(self, x:int,y:int,c:str):
        for p in self.pixels:
            if x == p.x and y == p.y:
                p.color = c

    def getPixelColor(self, x:int, y:int):
        for p in self.pixels:
            if x == p.x and y == p.y:
                return p.color

    def setAllPixelsColor(self, c:tuple):
        for p in self.pixels:
            p.color = c