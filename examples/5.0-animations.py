from src.Engine import Engine
from src.Levels.Level import Level
from src.Objects.Rectangle import Rectangle
from src.Player import Player
from src.Enums.Keys import Keys
from src.Keyboard import Keyboard
from src.Enums.EventType import EventType
from src.Textures.Texture import Texture
from src.Levels.LevelManager import LevelManager
from src.Utils.TerminalWindow import TerminalWindow
from src.Animations.Animation import Animation
from src.Animations.Keyframe import Keyframe

term = TerminalWindow()
TERM_WIDTH = term.getWidth()
TERM_HEIGHT = term.getHeight()

def make_level1():
    level = Level(TERM_WIDTH, TERM_HEIGHT)
    ground = Rectangle(0, TERM_HEIGHT - 3, TERM_WIDTH, 2, "=", fill=True)
    ground.setColor((100, 200, 100))
    ground.CanCollide = True
    ground.Anchored = True
    level.addObject(ground)

    plat = Rectangle(TERM_WIDTH // 10, TERM_HEIGHT - 10, TERM_WIDTH // 6, 1, "=", fill=True)
    plat.setColor((150, 150, 255))
    plat.CanCollide = True
    plat.Anchored = True
    level.addObject(plat)

    return level

def make_level2():
    level = Level(TERM_WIDTH, TERM_HEIGHT)
    ground = Rectangle(0, TERM_HEIGHT - 3, TERM_WIDTH, 2, "=", fill=True)
    ground.setColor((200, 100, 100))
    ground.CanCollide = True
    ground.Anchored = True
    level.addObject(ground)

    plat = Rectangle(TERM_WIDTH // 2, TERM_HEIGHT - 15, TERM_WIDTH // 5, 1, "=", fill=True)
    plat.setColor((255, 200, 100))
    plat.CanCollide = True
    plat.Anchored = True
    level.addObject(plat)

    return level

def make_level3():
    level = Level(TERM_WIDTH, TERM_HEIGHT)
    ground = Rectangle(0, TERM_HEIGHT - 3, TERM_WIDTH, 2, "=", fill=True)
    ground.setColor((100, 100, 200))
    ground.CanCollide = True
    ground.Anchored = True
    level.addObject(ground)

    plat = Rectangle(TERM_WIDTH * 3 // 4, TERM_HEIGHT - 20, TERM_WIDTH // 6, 1, "=", fill=True)
    plat.setColor((200, 100, 200))
    plat.CanCollide = True
    plat.Anchored = True
    level.addObject(plat)

    return level

def make_player():
    start_x = TERM_WIDTH // 20
    start_y = TERM_HEIGHT - 10
    root = Rectangle(start_x, start_y, 2, 7, "#", fill=True)
    root.setColor((100, 255, 255))
    root.CanCollide = True
    root.Anchored = False

    player = Player(root, x=start_x, y=start_y)

    head = Rectangle(start_x, start_y, 2, 2, "O", fill=True)
    left_leg = Rectangle(start_x, start_y + 5, 1, 2, "|", fill=True)
    right_leg = Rectangle(start_x + 1, start_y + 5, 1, 2, "|", fill=True)

    tex_left = Texture(2, 2)
    tex_right = Texture(2, 2)
    tex_left.setPixelColor(0, 0, (255, 255, 255)); tex_left.setPixelColor(1, 0, (100, 100, 100))
    tex_left.setPixelColor(0, 1, (255, 255, 255)); tex_left.setPixelColor(1, 1, (100, 100, 100))
    tex_right.setPixelColor(0, 0, (100, 100, 100)); tex_right.setPixelColor(1, 0, (255, 255, 255))
    tex_right.setPixelColor(0, 1, (100, 100, 100)); tex_right.setPixelColor(1, 1, (255, 255, 255))
    head.applyTexture(tex_right)

    player.tex_left = tex_left
    player.tex_right = tex_right

    COLOR_LEFT_STEP_1 = (150, 0, 0)
    COLOR_RIGHT_STEP_1 = (250, 0, 0)
    COLOR_LEFT_STEP_2 = (50, 0, 0)
    COLOR_RIGHT_STEP_2 = (150, 0, 0)

    tex_walk_1_left = Texture(1, 2); tex_walk_1_left.setAllPixelsColor(COLOR_LEFT_STEP_1)
    tex_walk_1_right = Texture(1, 2); tex_walk_1_right.setAllPixelsColor(COLOR_RIGHT_STEP_1)
    tex_walk_2_left = Texture(1, 2); tex_walk_2_left.setAllPixelsColor(COLOR_LEFT_STEP_2)
    tex_walk_2_right = Texture(1, 2); tex_walk_2_right.setAllPixelsColor(COLOR_RIGHT_STEP_2)

    tex_idle_left = Texture(1, 2); tex_idle_left.setAllPixelsColor((100, 0, 0))
    tex_idle_right = Texture(1, 2); tex_idle_right.setAllPixelsColor((200, 0, 0))

    left_leg.applyTexture(tex_idle_left)
    right_leg.applyTexture(tex_idle_right)

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

    walk_anim = Animation(loop=True)
    walk_anim.add_keyframe(Keyframe(0.0, target=left_leg, texture=tex_walk_1_left))
    walk_anim.add_keyframe(Keyframe(0.0, target=right_leg, texture=tex_walk_1_right))
    walk_anim.add_keyframe(Keyframe(0.2, target=left_leg, texture=tex_walk_2_left))
    walk_anim.add_keyframe(Keyframe(0.2, target=right_leg, texture=tex_walk_2_right))

    walk_anim.duration = 0.4

    root.add_animation("walk", walk_anim)

    player.spawn()

    root.addEvent(EventType.MOVING, lambda obj: player.sync_parts())

    return player

def main():
    engine = Engine(fps=30)
    manager = LevelManager(engine)

    levels = [make_level1(), make_level2(), make_level3()]
    player = make_player()
    manager.set_player(player)

    for lvl in levels:
        for part in player.objects.values():
            lvl.addObject(part)
        manager.add_level(lvl)

    manager.start(0)

    root = player.getoc("root")
    root.start_animation("walk")

    kb = Keyboard()

    def move_up():
        root = player.getoc("root")
        if root and root.is_grounded:
            root.vy = -player.getJumpVelocity()
            root.is_grounded = False

    def move_left():
        root = player.getoc("root")
        head = player.getoc("head")

        if head: head.applyTexture(player.tex_left)
        player.move(-player.getSpeed(), 0)

        root.start_animation("walk")

        if root.getX() <= 0:
            manager.change_level(manager.current_index - 1, TERM_WIDTH - 2)

    def move_right():
        root = player.getoc("root")
        head = player.getoc("head")

        if head: head.applyTexture(player.tex_right)
        player.move(player.getSpeed(), 0)

        root.start_animation("walk")

        if root.getX() >= TERM_WIDTH - 1:
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