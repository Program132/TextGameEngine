from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Rectangle import Rectangle
from src.EventType import EventType
from src.Textures.Texture import Texture
import random

move_counter = {"count": 0, "max": 17}

def on_moving(obj):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    obj.setColor((r, g, b))

    if obj.y < 3:
        obj.y += 0.3
    move_counter["count"] += 1

    if move_counter["count"] >= move_counter["max"]:
        obj.vx = 0
        obj.vy = 0
        obj.Anchored = True

def on_moved(obj):
    obj.setColor((0, 255, 0))

def main():
    engine = Engine()
    level = Level(20, 30)

    falling_rect = Rectangle(5, 0, 6, 6, "-", fill=True)
    falling_rect.vy = 0
    falling_rect.Anchored = False

    tex = Texture(falling_rect.width, falling_rect.height)
    tex.setAllPixelsColor((200, 200, 255))
    falling_rect.applyTexture(tex)

    falling_rect.addEvent(EventType.MOVING, on_moving)
    falling_rect.addEvent(EventType.MOVED, on_moved)
    level.addObject(falling_rect)

    engine.setLevel(level)

    try:
        engine.start()
    except KeyboardInterrupt:
        print("\n[Engine stopped]")

if __name__ == "__main__":
    main()
