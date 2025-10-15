from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Rectangle import Rectangle
from src.Player import Player
from src.Enums.Keys import Keys
from src.Keyboard import Keyboard
from src.Enums.EventType import EventType
from src.Textures.Texture import Texture
from src.Levels.LevelManager import LevelManager

def make_level1():
    level = Level(100, 40)
    ground = Rectangle(0, 38, 100, 2, "=", fill=True)
    ground.setColor((100, 200, 100))
    ground.CanCollide = True
    ground.Anchored = True
    level.addObject(ground)

    plat = Rectangle(20, 30, 15, 1, "=", fill=True)
    plat.setColor((150, 150, 255))
    plat.CanCollide = True
    plat.Anchored = True
    level.addObject(plat)

    return level

def make_level2():
    level = Level(100, 40)
    ground = Rectangle(0, 38, 100, 2, "=", fill=True)
    ground.setColor((200, 100, 100))
    ground.CanCollide = True
    ground.Anchored = True
    level.addObject(ground)

    plat = Rectangle(50, 25, 20, 1, "=", fill=True)
    plat.setColor((255, 200, 100))
    plat.CanCollide = True
    plat.Anchored = True
    level.addObject(plat)

    return level

def make_level3():
    level = Level(100, 40)
    ground = Rectangle(0, 38, 100, 2, "=", fill=True)
    ground.setColor((100, 100, 200))
    ground.CanCollide = True
    ground.Anchored = True
    level.addObject(ground)

    plat = Rectangle(70, 20, 15, 1, "=", fill=True)
    plat.setColor((200, 100, 200))
    plat.CanCollide = True
    plat.Anchored = True
    level.addObject(plat)

    return level

def make_player():
    root = Rectangle(5, 31, 2, 7, "#", fill=True)
    root.setColor((100, 255, 255))
    root.CanCollide = True
    root.Anchored = False

    player = Player(root, x=5, y=31)

    head = Rectangle(5, 31, 2, 2, "O", fill=True)
    left_leg = Rectangle(5, 36, 1, 2, "|", fill=True)
    right_leg = Rectangle(6, 36, 1, 2, "|", fill=True)

    tex_left = Texture(2, 2)
    tex_right = Texture(2, 2)
    tex_left.setPixelColor(0, 0, (255, 255, 255)); tex_left.setPixelColor(1, 0, (100, 100, 100))
    tex_left.setPixelColor(0, 1, (255, 255, 255)); tex_left.setPixelColor(1, 1, (100, 100, 100))
    tex_right.setPixelColor(0, 0, (100, 100, 100)); tex_right.setPixelColor(1, 0, (255, 255, 255))
    tex_right.setPixelColor(0, 1, (100, 100, 100)); tex_right.setPixelColor(1, 1, (255, 255, 255))
    head.applyTexture(tex_right)

    player.tex_left = tex_left
    player.tex_right = tex_right

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

    player.spawn()

    return player

def main():
    engine = Engine(fps=30)
    manager = LevelManager(engine)

    level1 = make_level1()
    level2 = make_level2()
    level3 = make_level3()

    player = make_player()
    manager.set_player(player)

    for lvl in [level1, level2, level3]:
        for part in player.objects.values():
            lvl.addObject(part)

    manager.add_level(level1)
    manager.add_level(level2)
    manager.add_level(level3)

    manager.start(0)

    kb = Keyboard()

    def move_up():
        root = player.getoc("root")
        if root and root.is_grounded:
            root.vy = -player.getJumpVelocity()
            root.is_grounded = False

    def move_left():
        head = player.getoc("head")
        if head: head.applyTexture(player.tex_left)
        player.move(-player.getSpeed(), 0)
        if player.getoc("root").getX() <= 0:
            manager.change_level(manager.current_index - 1, 99)

    def move_right():
        head = player.getoc("head")
        if head: head.applyTexture(player.tex_right)
        player.move(player.getSpeed(), 0)
        if player.getoc("root").getX() >= 99:
            manager.change_level(manager.current_index + 1, 1)

    kb.bind(Keys.W, move_up)
    kb.bind(Keys.A, move_left)
    kb.bind(Keys.D, move_right)

    try:
        engine.start()
    except KeyboardInterrupt:
        print("\n[Engine stopped]")

if __name__ == "__main__":
    main()
