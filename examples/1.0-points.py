from src.Levels.Level import Level
from src.Objects.Object import Object
from src.Objects.Point import Point
from src.Engine import Engine


def main():
    engine = Engine()

    level = Level(10, 5)

    red_point = Point(2, 1, "X", (255, 0, 0))
    green_point = Point(4, 2, "O", (0, 255, 0))
    blue_point = Point(6, 3, "#", (0, 0, 255))
    yellow_point = Point(8, 0, "@", (255, 255, 0))

    level.addObject(red_point)
    level.addObject(green_point)
    level.addObject(blue_point)
    level.addObject(yellow_point)

    engine.setLevel(level)

    engine.displayLevel()


if __name__ == "__main__":
    main()
