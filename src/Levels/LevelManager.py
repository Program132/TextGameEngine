from src.Engine import Engine
from src.Levels.Level import Level
from src.Player import Player

class LevelManager:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.levels = []
        self.current_index = 0
        self.player = None

    def add_level(self, level: Level):
        self.levels.append(level)

    def set_player(self, player: Player):
        self.player = player

    def start(self, index=0):
        self.current_index = index
        self.engine.setLevel(self.levels[self.current_index])

    def change_level(self, new_index, player_x=None):
        if 0 <= new_index < len(self.levels):
            self.current_index = new_index
            level = self.levels[self.current_index]

            for part in self.player.objects.values():
                if part in self.engine.currentLevel.objects:
                    self.engine.currentLevel.objects.remove(part)

            for part in self.player.objects.values():
                level.addObject(part)

            root = self.player.getoc("root")
            if root and player_x is not None:
                root.setX(player_x)
                self.player.sync_parts()

            self.engine.setLevel(level)