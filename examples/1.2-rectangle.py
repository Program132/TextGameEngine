from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Point import Point
from src.Objects.Rectangle import Rectangle
from src.Textures.Texture import Texture


def main():
    engine = Engine()
    level = Level(20, 10)

    texture = Texture(20, 10)
    texture.setPixelColor(2, 2, (255, 0, 0))
    texture.setPixelColor(3, 3, (0, 255, 0))
    texture.setPixelColor(4, 4, (0, 0, 255))

    rect = Rectangle(2, 2, 6, 4, "#", fill=True)
    rect.applyTexture(texture)

    level.addObject(rect)

    engine.setLevel(level)
    engine.start()


if __name__ == "__main__":
    main()
