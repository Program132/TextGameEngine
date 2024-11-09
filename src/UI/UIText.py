from src.Models import Point
from src.UI.Alignment import Alignment

class UIText:
    def __init__(self, x: int = 3, y: int = 0, sx: int = 6, sy: int = 1):
        self.pos_x = x
        self.pos_y = y
        self.size_x = sx
        self.size_y = sy
        self.alignment_x = Alignment.CENTER
        self.alignment_y = Alignment.CENTER
        self.text = "Text"
        self.borderLeftRightChar = "|"
        self.borderUpChar = "_"
        self.borderBottomChar = "¯"

    def getPosX(self):
        return self.pos_x

    def setPosX(self, x: int):
        self.pos_x = x

    def getPosY(self):
        return self.pos_y

    def setPosY(self, y: int):
        self.pos_y = y

    def getSizeX(self):
        return self.size_x

    def setSizeX(self, x: int):
        self.size_x = x

    def getSizeY(self):
        return self.size_y

    def setSizeY(self, y: int):
        self.size_y = y

    def getAlignmentX(self):
        return self.alignment_x

    def setAlignmentX(self, alignment):
        self.alignment_x = alignment

    def getAlignmentY(self):
        return self.alignment_y

    def setAlignmentY(self, alignment):
        self.alignment_y = alignment

    def getText(self):
        return self.text

    def setText(self, text: str):
        self.text = text

    def getBorderLeftRightChar(self):
        return self.borderLeftRightChar

    def setBorderLeftRightChar(self, char: str):
        self.borderLeftRightChar = char

    def getBorderUpChar(self):
        return self.borderUpChar

    def setBorderUpChar(self, char: str):
        self.borderUpChar = char

    def getBorderBottomChar(self):
        return self.borderBottomChar

    def setBorderBottomChar(self, char: str):
        self.borderBottomChar = char

    def getPoints(self):
        points = []
        text_length = len(self.text)

        def get_text_start_x(lineText):
            if self.alignment_x == Alignment.LEFT:
                return 1
            elif self.alignment_x == Alignment.CENTER:
                return (self.size_x - len(lineText)) // 2
            elif self.alignment_x == Alignment.RIGHT:
                return self.size_x - len(lineText) - 1
            else:
                return 1

        max_text_width = self.size_x - 2
        lines = [self.text[i:i + max_text_width] for i in range(0, text_length, max_text_width)]

        if self.alignment_y == Alignment.TOP:
            text_start_y = 1
        elif self.alignment_y == Alignment.CENTER:
            text_start_y = (self.size_y - len(lines)) // 2 + 1
        elif self.alignment_y == Alignment.BOTTOM:
            text_start_y = self.size_y - len(lines) + 1
        else:
            text_start_y = 1

        for x in range(self.size_x):
            points.append(Point(self.pos_x + x, self.pos_y, self.borderUpChar))

        for y in range(1, self.size_y + 1):
            points.append(Point(self.pos_x, self.pos_y + y, self.borderLeftRightChar))
            if text_start_y <= y < text_start_y + len(lines):
                line_text = lines[y - text_start_y]
                start_x = get_text_start_x(line_text)
                for i, char in enumerate(line_text):
                    points.append(Point(self.pos_x + start_x + i, self.pos_y + y, char))
                for x in range(1, start_x):
                    points.append(Point(self.pos_x + x, self.pos_y + y, ' '))
                for x in range(start_x + len(line_text), self.size_x - 1):
                    points.append(Point(self.pos_x + x, self.pos_y + y, ' '))
            else:
                for x in range(1, self.size_x - 1):
                    points.append(Point(self.pos_x + x, self.pos_y + y, ' '))
            points.append(Point(self.pos_x + self.size_x - 1, self.pos_y + y, self.borderLeftRightChar))

        for x in range(self.size_x):
            points.append(Point(self.pos_x + x, self.pos_y + self.size_y + 1, self.borderBottomChar))

        return points
