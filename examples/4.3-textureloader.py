from src.Engine import Engine
from src.LevelLoader import LevelLoader
from src.Enums.Keys import Keys
from src.Keyboard import Keyboard
from src.Enums.EventType import EventType
from src.Textures.TextureLoader import TextureLoader

def main():
    engine = Engine(fps=30)
    level, player = LevelLoader.load_from_json("./level1.json")
    textures = TextureLoader.load_from_file("./texture.json")

    head = player.getoc("head")
    if head:
        head.applyTexture(textures["player_head_right"])

    kb = Keyboard()

    def move_up():
        root_obj = player.getoc("root")
        if root_obj and root_obj.is_grounded:
            root_obj.vy = -player.getJumpVelocity()
            root_obj.is_grounded = False

    def move_left():
        head = player.getoc("head")
        if head:
            head.applyTexture(textures["player_head_left"])
        player.move(-player.getSpeed(), 0)

    def move_right():
        head = player.getoc("head")
        if head:
            head.applyTexture(textures["player_head_right"])
        player.move(player.getSpeed(), 0)

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


# texture.json:
texture = {
    "player_head_left": {
        "width": 2,
        "height": 2,
        "pixels": [
            [[255, 255, 255], [100, 100, 100]],
            [[255, 255, 255], [100, 100, 100]]
        ]
    },
    "player_head_right": {
        "width": 2,
        "height": 2,
        "pixels": [
            [[100, 100, 100], [255, 255, 255]],
            [[100, 100, 100], [255, 255, 255]]
        ]
    }
}
