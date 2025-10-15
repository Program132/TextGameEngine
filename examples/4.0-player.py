from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Rectangle import Rectangle
from src.Player import Player
from src.Enums.Keys import Keys
from src.Keyboard import Keyboard
from src.Textures.Texture import Texture


def main():
    engine = Engine(fps=20)
    level = Level(40, 25)

    ground = Rectangle(0, 20, 40, 5, "=", fill=True)
    ground.setColor((100, 200, 100))
    ground.CanCollide = True
    ground.Anchored = True
    level.addObject(ground)



    root = Rectangle(10, 5, 4, 4, "#", fill=True)
    player = Player(root, x=10, y=5)
    head = Rectangle(11, 3, 2, 2, "O", fill=True)
    left_leg = Rectangle(10, 9, 1, 3, "|", fill=True)
    right_leg = Rectangle(13, 9, 1, 3, "|", fill=True)

    root.setColor( (100,255,255) )
    head.setColor( (100,100,100) )
    left_leg.setColor( (100,0,0) )
    right_leg.setColor( (200,0,0) )

    tex_left = Texture(2, 2)
    tex_left.setPixelColor(0, 0, (255, 255, 255))
    tex_left.setPixelColor(1, 0, (100,100,100))
    tex_left.setPixelColor(0, 1, (255, 255, 255))
    tex_left.setPixelColor(1, 1, (100,100,100))
    tex_right = Texture(2, 2)
    tex_right.setPixelColor(0, 0, (100,100,100))
    tex_right.setPixelColor(1, 0, (255, 255, 255))
    tex_right.setPixelColor(0, 1, (100,100,100))
    tex_right.setPixelColor(1, 1, (255, 255, 255))

    root.CanCollide = True
    head.CanCollide = True
    left_leg.CanCollide = True
    right_leg.CanCollide = True

    root.Anchored = False
    head.Anchored = False
    left_leg.Anchored = False
    right_leg.Anchored = False

    player.setoc("root", root)
    player.setoc("head", head)
    player.setoc("left_leg", left_leg)
    player.setoc("right_leg", right_leg)



    for part in player.objects.values():
        level.addObject(part)
    kb = Keyboard()

    def move_up():
        player.move(0, -1)

    def move_down():
        player.move(0, 1)

    def move_left():
        head.applyTexture(tex_left)
        player.setoc("head", head)
        player.move(-1, 0)

    def move_right():
        head.applyTexture(tex_right)
        player.setoc("head", head)
        player.move(1, 0)

    kb.bind(Keys.W, move_up)
    kb.bind(Keys.S, move_down)
    kb.bind(Keys.A, move_left)
    kb.bind(Keys.D, move_right)


    engine.setLevel(level)
    try:
        engine.start()
    except KeyboardInterrupt:
        print("\n[Engine stopped]")


if __name__ == "__main__":
    main()
