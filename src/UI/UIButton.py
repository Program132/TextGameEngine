from src.UI.UIText import UIText
import keyboard

class UIButton(UIText):
    def __init__(self, x: int = 3, y: int = 0, sx: int = 6, sy: int = 1, key: str = 'S'):
        super().__init__(x, y, sx, sy)
        self.key = key.lower()
        self.text += f" ({self.key})"
        self.on_click_callback = None
        self.is_pressed = False

    def setOnClick(self, callback):
        if callable(callback):
            self.on_click_callback = callback

    def listenForClick(self):
        if keyboard.is_pressed(self.key):
            if not self.is_pressed:
                self.is_pressed = True
                if self.on_click_callback is not None and callable(self.on_click_callback):
                    self.on_click_callback()
        else:
            self.is_pressed = False

    def getKey(self):
        return self.key

    def setKey(self, key: str):
        self.key = key
        self.text = self.text.split(" (")[0] + f" ({self.key})"