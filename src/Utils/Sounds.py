import simpleaudio as sa
import threading
import time

class Sounds:
    def __init__(self, pathSound: str = "", repeat: bool = False):
        self.pathSound = pathSound
        self.repeat = repeat
        self.audio = None
        self.is_playing = False
        self._thread = None

    def _play_loop(self):
        try:
            wave_obj = sa.WaveObject.from_wave_file(self.pathSound)
            while self.is_playing:
                self.audio = wave_obj.play()
                self.audio.wait_done()
                if not self.repeat:
                    break
        except FileNotFoundError:
            print(f"[Sound] File not found: {self.pathSound}")

    def play(self):
        if not self.pathSound or self.is_playing:
            return
        self.is_playing = True
        self._thread = threading.Thread(target=self._play_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self.is_playing = False
        if self.audio:
            self.audio.stop()

    def setPath(self, path: str):
        self.pathSound = path

    def getPath(self):
        return self.pathSound
