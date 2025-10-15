from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Rectangle import Rectangle
from src.Textures.Texture import Texture


def main():
    engine = Engine()
    level = Level(15, 8)

    texture = Texture(20, 10)
    texture.setAllPixelsColor((130, 130, 200))

    rect = Rectangle(2, 2, 6, 4, "#", fill=False)
    rect.applyTexture(texture)

    level.addObject(rect)

    engine.setLevel(level)
    engine.start()


if __name__ == "__main__":
    main()
