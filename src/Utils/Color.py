class Color:
    def __init__(self, r: int, g:int, b:int):
        self.r = r
        self.g = g
        self.b = b

    def get(self):
        return (self.r, self.g, self.b)