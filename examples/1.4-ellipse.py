from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Ellipse import Ellipse
from src.Textures.Texture import Texture

def main():
    engine = Engine()
    level = Level(25, 15)

    texture = Texture(25, 15)
    texture.setAllPixelsColor((0, 255, 0))  # vert

    ellipse = Ellipse(5, 5, 15, 6, "E", fill=True)
    ellipse.applyTexture(texture)

    level.addObject(ellipse)

    engine.setLevel(level)
    engine.start()

if __name__ == "__main__":
    main()
