from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Rectangle import Rectangle
from src.EventType import EventType
from src.Textures.Texture import Texture

def touching_color(obj, other):
    tex = Texture(20, 10)
    tex.setAllPixelsColor((255,0,0))
    obj.applyTexture(tex)

def main():
    engine = Engine()
    level = Level(20, 30)

    ground = Rectangle(0, 25, 20, 1, "#", fill=True)
    ground.Anchored = True

    falling_rect = Rectangle(5, 0, 6, 6, "-", fill=True)
    falling_rect.vy = 5
    falling_rect.Anchored = False
    falling_rect.addEvent(EventType.TOUCHED, touching_color)

    tex = Texture(20, 10)
    tex.setAllPixelsColor((200,200,255))
    falling_rect.applyTexture(tex)

    level.addObject(ground)
    level.addObject(falling_rect)

    engine.setLevel(level)

    try:
        engine.start()
    except KeyboardInterrupt:
        print("\n[Engine stopped]")

if __name__ == "__main__":
    main()
