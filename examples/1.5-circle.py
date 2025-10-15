from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Circle import Circle
from src.Textures.Texture import Texture

def main():
    engine = Engine()
    level = Level(20, 15)

    texture = Texture(20, 15)
    texture.setAllPixelsColor((255, 0, 0))

    circle = Circle(5, 5, 2, "O", fill=True)
    circle.applyTexture(texture)

    level.addObject(circle)

    engine.setLevel(level)
    engine.start()

if __name__ == "__main__":
    main()
