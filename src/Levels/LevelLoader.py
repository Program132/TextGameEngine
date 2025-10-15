import json
from src.Level import Level
from src.Objects.Rectangle import Rectangle
from src.Player import Player

class LevelLoader:
    @staticmethod
    def load_from_json(file_path: str):
        with open(file_path, "r") as f:
            data = json.load(f)

        level = Level(data["width"], data["height"])

        px, py = data["player"]["x"], data["player"]["y"]
        root_cfg = data["player"]["root"]
        root = Rectangle(px, py, root_cfg["w"], root_cfg["h"], root_cfg["char"], fill=True)
        root.setColor(tuple(root_cfg["color"]))
        root.Anchored = False
        root.CanCollide = True

        player = Player(root, x=px, y=py)
        player.setoc("root", root)

        for name, part_cfg in data["player"]["parts"].items():
            part = Rectangle(
                px + part_cfg["dx"],
                py + part_cfg["dy"],
                part_cfg["w"],
                part_cfg["h"],
                part_cfg["char"],
                fill=True
            )
            part.setColor(tuple(part_cfg["color"]))
            part.Anchored = True
            part.CanCollide = False
            player.setoc(name, part)
            player.set_part_offset(name, part_cfg["dx"], part_cfg["dy"])

        for part in player.objects.values():
            level.addObject(part)

        for obj_cfg in data["objects"]:
            obj = Rectangle(obj_cfg["x"], obj_cfg["y"], obj_cfg["w"], obj_cfg["h"], obj_cfg["char"], fill=True)
            obj.setColor(tuple(obj_cfg["color"]))
            obj.Anchored = obj_cfg.get("anchored", True)
            obj.CanCollide = True
            level.addObject(obj)

        return level, player
