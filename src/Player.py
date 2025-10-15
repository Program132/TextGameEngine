from src.Objects.Object import Object
from typing import Dict, Tuple
from src.Enums.EventType import EventType

class Player:
    def __init__(self, character: 'Object', x: int = 0, y: int = 0, health: int = 100):
        self.character = character
        self.x = x
        self.y = y
        self.objects: Dict[str, 'Object'] = {}
        self.offsets: Dict[str, Tuple[float, float]] = {}
        self.health = health
        self.speed = 1.0
        self.jump_velocity = 12.0
        self.moving_left = False
        self.moving_right = False
        self.setObjectFromCharacter("root", character)
        self.character.setX(x)
        self.character.setY(y)

        self.character.addEvent(EventType.MOVING, lambda obj: self.sync_parts())

    def setObjectFromCharacter(self, name: str, o: 'Object'):
        self.objects[name] = o

    def removeObjectFromCharacter(self, name: str):
        if name in self.objects:
            del self.objects[name]

    def getObjectFromCharacter(self, name: str) -> 'Object':
        return self.objects.get(name)

    def set_part_offset(self, part_name: str, dx: float, dy: float):
        self.offsets[part_name] = (dx, dy)

    def get_part_offset(self, part_name: str) -> Tuple[float, float]:
        return self.offsets.get(part_name, (0.0, 0.0))

    def sync_parts(self, root_x: float = None, root_y: float = None):
        root = self.character
        new_root_x = root_x if root_x is not None else root.getX()
        new_root_y = root_y if root_y is not None else root.getY()

        if root_x is not None:
            root.setX(new_root_x)
        if root_y is not None:
            root.setY(new_root_y)

        for name, part in self.objects.items():
            if name != "root":
                if name in self.offsets:
                    dx, dy = self.offsets[name]
                    part.setX(new_root_x + dx)
                    part.setY(new_root_y + dy)

    def move(self, dx: float, dy: float):
        self.character.setX(self.character.getX() + dx)
        self.character.setY(self.character.getY() + dy)
        self.sync_parts()

    def spawn(self):
        self.character.setX(self.x)
        self.character.setY(self.y)
        self.sync_parts()

    def getHealth(self): return self.health
    def setHealth(self, x: int): self.health = x
    def getSpeed(self): return self.speed
    def setSpeed(self, x: float): self.speed = x
    def getJumpVelocity(self): return self.jump_velocity
    def setJumpVelocity(self, x: float): self.jump_velocity = x

    setoc = setObjectFromCharacter
    remoc = removeObjectFromCharacter
    getoc = getObjectFromCharacter