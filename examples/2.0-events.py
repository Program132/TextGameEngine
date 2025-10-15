from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Point import Point
from src.EventType import EventType
from src.Textures.Texture import Texture

def change_color_on_touch(obj, other):
    obj.color = (255,0,0)

def main():
    engine = Engine()
    level = Level(20, 10)

    ground = Point(10, 8, "#")
    ground.Anchored = True

    ball = Point(10, 0, "O")
    ball.vy = 5
    ball.Anchored = False
    ball.addEvent(EventType.TOUCHED, change_color_on_touch)

    level.addObject(ground)
    level.addObject(ball)

    engine.setLevel(level)

    try:
        engine.start()
    except KeyboardInterrupt:
        print("\n[Engine stopped]")

if __name__ == "__main__":
    main()
