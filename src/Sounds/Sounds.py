import simpleaudio as sa

class Sounds:
    def __init__(self, pathSound: str = "", repeat: bool = False):
        self.pathSound = pathSound
        self.repeat = repeat
        self.audio = None
        self.is_playing = False

    def play(self):
        if self.pathSound:
            try:
                wave_obj = sa.WaveObject.from_wave_file(self.pathSound)
                play_count = -1 if self.repeat else 1
                for _ in range(play_count):
                    self.audio = wave_obj.play()
                    self.audio.wait_done()
                self.is_playing = True
            except FileNotFoundError:
                print(f"File not found: {self.pathSound}")

    def stop(self):
        if self.audio and self.is_playing:
            self.audio.stop()
            self.is_playing = False

    def setPath(self, path: str):
        self.pathSound = path

    def getPath(self):
        return self.pathSound