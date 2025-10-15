class Level:
    def __init__(self, sx: int, sy: int):
        self.size_x = sx
        self.size_y = sy
        self.objects = []
        self.player = None

    def set_player(self, player):
        self.player = player

    def addObject(self, o):
        self.objects.append(o)

    def update(self, delta):
        for obj in self.objects:
            obj.update(delta, self)

    def display(self):
        grid = [[" " for _ in range(self.size_x)] for _ in range(self.size_y)]

        for obj in self.objects:
            for (x, y, char) in obj.getPoints():
                if 0 <= x < self.size_x and 0 <= y < self.size_y:
                    if isinstance(char, tuple) and char[1] is not None:
                        ch, rgb = char
                        r, g, b = rgb
                        grid[int(y)][int(x)] = f"\033[38;2;{r};{g};{b}m{ch}\033[0m"
                    else:
                        grid[int(y)][int(x)] = str(char if not isinstance(char, tuple) else char[0])

        print("\033[H\033[J", end="")
        for row in grid:
            print("".join(row))