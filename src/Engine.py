import time


class Engine:
    def __init__(self, fps: int = 20):
        self.currentLevel = None
        self.running = True
        self.fps = fps
        self.last_time = None

    def setLevel(self, level):
        self.currentLevel = level

    def update(self, delta):
        if self.currentLevel:
            self.currentLevel.update(delta)

    def display(self):
        if self.currentLevel:
            self.currentLevel.display()

    def start(self, duration: float = None):
        first_frame = True
        self.last_time = time.time()
        start_time = self.last_time
        while self.running:
            now = time.time()
            delta = now - self.last_time
            self.last_time = now

            self.update(delta)

            if not first_frame:
                print("\033[H\033[J", end="")
            first_frame = False

            self.display()

            if duration is not None and (now - start_time) >= duration:
                break

            frame_time = 1.0 / self.fps
            elapsed = time.time() - now
            time.sleep(max(0.0, frame_time - elapsed))