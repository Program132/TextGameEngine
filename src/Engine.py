import os
import time


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Engine:
    def __init__(self, x=20, y=8, c='.'):
        self.size_x = x
        self.size_y = y
        self.objects = []
        self.char = c
        self.mainLevel = None

    def getSizeX(self):
        return self.size_x

    def getSizeY(self):
        return self.size_y

    def getChar(self):
        return self.char

    def display(self):
        if self.mainLevel is not None:
            self.mainLevel.display()

    def refresh(self, delay: float = 0.05):
        clear_screen()
        self.display()
        time.sleep(delay)

    def setCurrentLevel(self, l):
        self.mainLevel = l
