import keyboard

class Inputs:
    def __init__(self, key: str, callback):
        self.key = key.lower()
        self.callback = callback if callable(callback) else None
        self.is_pressed = False

    def listenForInput(self):
        if keyboard.is_pressed(self.key):
            if not self.is_pressed:
                self.is_pressed = True
                if self.callback is not None:
                    self.callback()
        else:
            self.is_pressed = False

    def setKey(self, key: str):
        self.key = key.lower()

    def setCallback(self, callback):
        if callable(callback):
            self.callback = callback

    def getKey(self):
        return self.key