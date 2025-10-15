from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Square import Square
from src.Textures.Texture import Texture

def main():
    engine = Engine()
    level = Level(20, 15)

    texture = Texture(20, 15)
    texture.setAllPixelsColor((0, 0, 255))

    square = Square(5, 5, 2, "#", fill=True)
    square.applyTexture(texture)

    level.addObject(square)

    engine.setLevel(level)
    engine.start()

if __name__ == "__main__":
    main()
