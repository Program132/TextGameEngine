from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Point import Point
from src.Textures.Texture import Texture


def main():
    engine = Engine()
    level = Level(10, 5)

    texture = Texture(10, 5)
    texture.setPixelColor(2, 1, (255, 0, 0))
    texture.setPixelColor(4, 2, (0, 255, 0))
    texture.setPixelColor(6, 3, (0, 0, 255))
    texture.setPixelColor(8, 0, (255, 255, 0))

    p1 = Point(2, 1, "X")
    p2 = Point(4, 2, "O")
    p3 = Point(6, 3, "#")
    p4 = Point(8, 0, "@")

    for p in [p1, p2, p3, p4]:
        p.applyTexture(texture)
        level.addObject(p)

    engine.setLevel(level)
    engine.displayLevel()


if __name__ == "__main__":
    main()