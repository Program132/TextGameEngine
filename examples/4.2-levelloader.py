from src.Engine import Engine
from src.Levels.LevelLoader import LevelLoader
from src.Enums.Keys import Keys
from src.Keyboard import Keyboard
from src.Enums.EventType import EventType
from src.Textures.Texture import Texture

JUMP_VELOCITY = 12.0
MOVE_SPEED = 1

def main():
    engine = Engine(fps=30)

    level, player = LevelLoader.load_from_json("./level1.json")

    tex_left = Texture(2, 2)
    tex_right = Texture(2, 2)
    tex_left.setPixelColor(0, 0, (255, 255, 255)); tex_left.setPixelColor(1, 0, (100, 100, 100))
    tex_left.setPixelColor(0, 1, (255, 255, 255)); tex_left.setPixelColor(1, 1, (100, 100, 100))
    tex_right.setPixelColor(0, 0, (100, 100, 100)); tex_right.setPixelColor(1, 0, (255, 255, 255))
    tex_right.setPixelColor(0, 1, (100, 100, 100)); tex_right.setPixelColor(1, 1, (255, 255, 255))

    head = player.getoc("head")
    if head: head.applyTexture(tex_right)

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


# level1.json:
level1 = {
    "width": 100,
    "height": 40,
    "player": {
        "x": 5,
        "y": 31,
        "root": { "w": 2, "h": 7, "char": "#", "color": [100, 255, 255] },
        "parts": {
            "head": { "dx": 0, "dy": 0, "w": 2, "h": 2, "char": "O", "color": [255, 255, 255] },
            "left_leg": { "dx": 0, "dy": 5, "w": 1, "h": 2, "char": "|", "color": [100, 0, 0] },
            "right_leg": { "dx": 1, "dy": 5, "w": 1, "h": 2, "char": "|", "color": [200, 0, 0] }
        }
    },
    "objects": [
        {
            "x": 0, "y": 38, "w": 100, "h": 2, "char": "=", "color": [100, 200, 100], "anchored": true
        },
        {
            "x": 15, "y": 30, "w": 20, "h": 1, "char": "=", "color": [150, 150, 255], "anchored": true
        },
        {
            "x": 50, "y": 25, "w": 15, "h": 1, "char": "=", "color": [255, 200, 100], "anchored": true
        },
        {
            "x": 75, "y": 20, "w": 10, "h": 1, "char": "=", "color": [200, 100, 200], "anchored": true
        }
    ]
}
