class Player:
    def __init__(self, x: int = 0, y: int = 0, c: str = 'P'):
        self.health = 100
        self.pos_x = x
        self.pos_y = y
        self.char = c

    def getHealth(self):
        return self.health

    def getX(self):
        return self.pos_x

    def getY(self):
        return self.pos_y

    def getChar(self):
        return self.char

    def setHealth(self, health: int):
        self.health = health

    def setX(self, x: int):
        self.pos_x = x

    def setY(self, y: int):
        self.pos_y = y

    def setChar(self, c: str):
        self.char = c

    def moveLeft(self):
        self.pos_x -= 1

    def moveRight(self):
        self.pos_x += 1

    def moveUp(self):
        self.pos_y -= 1

    def moveDown(self):
        self.pos_y += 1

    def inflictDamage(self, h: int = 10):
        self.health -= h

    def addHealth(self, h: int = 10):
        self.health += h

    def isDead(self):
        return self.health <= 0

    def teleportTo(self, x: int, y: int):
        self.pos_x = x
        self.pos_y = y
