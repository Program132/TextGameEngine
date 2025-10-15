from src.Engine import Engine
from src.UI.UILevel import UILevel
from src.UI.Text import Text
from src.UI.TextAsciiArt import TextAsciiArt
from src.UI.Button import Button
from src.UI.UIObject import UIObject
from src.Utils.TerminalWindow import TerminalWindow
from src.Levels.Level import Level
from src.Objects.Rectangle import Rectangle
from src.Player import Player
from src.Enums.Keys import Keys
from src.Keyboard import Keyboard
from src.Enums.EventType import EventType
from src.Textures.Texture import Texture
from src.Levels.LevelManager import LevelManager
from src.Animations.Animation import Animation
from src.Animations.Keyframe import Keyframe
from src.Utils.Sounds import Sounds
import time
import random

term = TerminalWindow()
TERM_WIDTH = term.getWidth()
TERM_HEIGHT = term.getHeight()

global_player = None
global_manager = None
global_engine = None

def get_random_rgb():
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    return (r, g, b)

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

    walk_anim.add_keyframe(Keyframe(0.0, target=head, dy=0))
    walk_anim.add_keyframe(Keyframe(0.2, target=head, dy=-1))

    walk_anim.duration = 0.4
    root.add_animation("walk", walk_anim)

    idle_anim = Animation(loop=True)
    idle_anim.duration = 1.0
    idle_anim.add_keyframe(Keyframe(0.0, target=left_leg, texture=tex_idle_left))
    idle_anim.add_keyframe(Keyframe(0.0, target=right_leg, texture=tex_idle_right))
    idle_anim.add_keyframe(Keyframe(0.0, target=head, dy=0))
    root.add_animation("idle", idle_anim)

    player.spawn()
    root.addEvent(EventType.MOVED, lambda obj: obj.start_animation("idle", force_restart=True))

    return player

def start_game_loop():
    global global_player, global_manager, global_engine

    engine = Engine(fps=30)
    global_engine = engine

    manager = LevelManager(engine)
    global_manager = manager

    levels = [make_level1(), make_level2(), make_level3()]
    player = make_player()
    global_player = player

    manager.set_player(player)

    for lvl in levels:
        for part in player.objects.values():
            lvl.addObject(part)
        manager.add_level(lvl)

    manager.start(0)

    root = player.getoc("root")
    root.start_animation("idle", force_restart=True)

    kb = Keyboard()

    def move_up():
        root = global_player.getoc("root")
        if root and root.is_grounded:
            root.vy = -global_player.getJumpVelocity()
            root.is_grounded = False

    def move_left():
        root = global_player.getoc("root")
        head = global_player.getoc("head")
        if head: head.applyTexture(global_player.tex_left)
        global_player.move(-global_player.getSpeed(), 0)
        root.start_animation("walk")
        if root.getX() <= 0:
            global_manager.change_level(global_manager.current_index - 1, TERM_WIDTH - 2)

    def move_right():
        root = global_player.getoc("root")
        head = global_player.getoc("head")
        if head:
            head.applyTexture(global_player.tex_right)
        global_player.move(global_player.getSpeed(), 0)
        root.start_animation("walk")
        if root.getX() >= TERM_WIDTH - 1:
            global_manager.change_level(global_manager.current_index + 1, 1)

    kb.bind(Keys.W, move_up)
    kb.bind(Keys.A, move_left)
    kb.bind(Keys.D, move_right)

    try:
        engine.start()
    except KeyboardInterrupt:
        print("\n[Engine stopped]")

def main_menu():
    global global_engine

    ui_level = UILevel()
    ui_level.term_cols = TERM_WIDTH
    ui_level.term_rows = TERM_HEIGHT

    def handle_button_click():
        global global_engine

        new_color = get_random_rgb()
        button.set_color(new_color)

        if global_engine:
            global_engine.running = False

        return start_game_loop

    title = TextAsciiArt(
        "TextGameEngine",
        font="slant",
        color=(0, 255, 255),
        x=0, y=2,
        align_x=UIObject.Alignment.CENTER,
        align_y=UIObject.Alignment.TOP
    )

    button = Button(
        "Start",
        on_click=handle_button_click,
        x=0, y=TERM_HEIGHT//2,
        align_x=UIObject.Alignment.CENTER,
        align_y=UIObject.Alignment.TOP,
        color=(255, 255, 255)
    )

    ui_level.addObject(title)
    ui_level.addObject(button)

    engine = Engine(fps=10)
    global_engine = engine
    engine.setLevel(ui_level)

    try:
        engine.start()
    except KeyboardInterrupt:
        print("\n[Engine stopped]")

    if not global_engine or not global_engine.running:
        start_game_loop()

if __name__ == "__main__":
    main_menu()