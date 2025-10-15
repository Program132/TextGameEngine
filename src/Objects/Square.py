from src.Objects.Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, x: int, y: int, size: int, char: str = "*", fill: bool = True):
        super().__init__(x, y, size, size, char, fill)
