import sys, termios, tty, select, threading
from src.Enums.Keys import Keys

class Keyboard:
    def __init__(self):
        self.bindings = {}
        self.running = True
        self.thread = threading.Thread(target=self._listen, daemon=True)
        self.thread.start()

    def bind(self, key: Keys, func):
        if key not in self.bindings:
            self.bindings[key] = []
        self.bindings[key].append(func)

    def _listen(self):
        old_settings = termios.tcgetattr(sys.stdin)
        try:
            tty.setcbreak(sys.stdin.fileno())
            while self.running:
                dr, _, _ = select.select([sys.stdin], [], [], 0.05)
                if dr:
                    key = sys.stdin.read(1)
                    if key == "\x1b":
                        seq = sys.stdin.read(2)
                        if seq == "[A":
                            self._trigger(Keys.UP)
                        elif seq == "[B":
                            self._trigger(Keys.DOWN)
                        elif seq == "[C":
                            self._trigger(Keys.RIGHT)
                        elif seq == "[D":
                            self._trigger(Keys.LEFT)
                        else:
                            self._trigger(Keys.ESC)
                    else:
                        for enum_key in Keys:
                            if enum_key.value == key:
                                self._trigger(enum_key)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    def _trigger(self, key: Keys):
        if key in self.bindings:
            for func in self.bindings[key]:
                func()

    def stop(self):
        self.running = False
