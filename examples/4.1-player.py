from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Rectangle import Rectangle
from src.Objects.Object import Object
from src.Player import Player
from src.Enums.Keys import Keys
from src.Keyboard import Keyboard
from src.Textures.Texture import Texture
from src.Enums.EventType import EventType

JUMP_VELOCITY = 12.0
MOVE_SPEED = 1

def main():
    engine = Engine(fps=30)
    level = Level(100, 40)

    ground = Rectangle(0, 38, 100, 2, "=", fill=True)
    ground.setColor((100, 200, 100))
    ground.CanCollide = True
    ground.Anchored = True
    level.addObject(ground)

    for x, y, w, color in [(15, 30, 20, (150, 150, 255)), (50, 25, 15, (255, 200, 100)), (75, 20, 10, (200, 100, 200))]:
        plat = Rectangle(x, y, w, 1, "=", fill=True)
        plat.setColor(color)
        plat.CanCollide = True
        plat.Anchored = True
        level.addObject(plat)

    start_x, start_y = 5, 31
    root = Rectangle(start_x, start_y, 2, 7, "#", fill=True)
    root.setColor((100, 255, 255))
    root.CanCollide = True
    root.Anchored = False

    player = Player(root, x=start_x, y=start_y)

    head = Rectangle(start_x, start_y, 2, 2, "O", fill=True)
    left_leg = Rectangle(start_x, start_y, 1, 2, "|", fill=True)
    right_leg = Rectangle(start_x, start_y, 1, 2, "|", fill=True)

    tex_left = Texture(2, 2)
    tex_right = Texture(2, 2)
    tex_left.setPixelColor(0, 0, (255, 255, 255)); tex_left.setPixelColor(1, 0, (100, 100, 100))
    tex_left.setPixelColor(0, 1, (255, 255, 255)); tex_left.setPixelColor(1, 1, (100, 100, 100))
    tex_right.setPixelColor(0, 0, (100, 100, 100)); tex_right.setPixelColor(1, 0, (255, 255, 255))
    tex_right.setPixelColor(0, 1, (100, 100, 100)); tex_right.setPixelColor(1, 1, (255, 255, 255))
    head.applyTexture(tex_right)

    left_leg.setColor((100, 0, 0))
    right_leg.setColor((200, 0, 0))

    head.CanCollide = False
    left_leg.CanCollide = False
    right_leg.CanCollide = False
    head.Anchored = True
    left_leg.Anchored = True
    right_leg.Anchored = True

    player.setoc("head", head)
    player.setoc("left_leg", left_leg)
    player.setoc("right_leg", right_leg)

    player.set_part_offset("head", 0, 0)
    player.set_part_offset("left_leg", 0, 5)
    player.set_part_offset("right_leg", 1, 5)

    for part in player.objects.values():
        level.addObject(part)

    player.spawn()

    kb = Keyboard()

    def move_up():
        root_obj = player.getoc("root")
        if root_obj and root_obj.is_grounded:
            root_obj.vy = -JUMP_VELOCITY
            root_obj.is_grounded = False

    def move_left():
        head = player.getoc("head")
        if head: head.applyTexture(tex_left)
        player.move(-MOVE_SPEED, 0)

    def move_right():
        head = player.getoc("head")
        if head: head.applyTexture(tex_right)
        player.move(MOVE_SPEED, 0)

    kb.bind(Keys.W, move_up)
    kb.bind(Keys.A, move_left)
    kb.bind(Keys.D, move_right)

    engine.setLevel(level)

    try:
        engine.start()
    except KeyboardInterrupt:
        print("\n[Engine stopped]")

if __name__ == "__main__":
    main()