import os
import shutil
import subprocess
import time

class TerminalWindow:
    def __init__(self):
        self.__updateSize()
        self.char_width_pixel = 0
        self.char_height_pixel = 0
        self.x_screen = 0
        self.y_screen = 0
        self.__updateScreenInfo()

    def __updateSize(self):
        try:
            size = shutil.get_terminal_size()
            self.width = size.columns
            self.height = size.lines
        except OSError:
            self.width = 80
            self.height = 24

    def __get_window_position_xdotool(self):
        try:
            window_id = subprocess.check_output(['xdotool', 'getactivewindow'], text=True).strip()
            geometry = subprocess.check_output(['xdotool', 'getwindowgeometry', '--shell', window_id], text=True).strip()
            x, y = 0, 0
            for line in geometry.split('\n'):
                if line.startswith('X='):
                    x = int(line.split('=')[1])
                elif line.startswith('Y='):
                    y = int(line.split('=')[1])
            return x, y
        except Exception:
            return 0, 0

    def __get_char_size(self):
        try:
            window_id = subprocess.check_output(['xdotool', 'getactivewindow'], text=True).strip()
            geometry = subprocess.check_output(['xdotool', 'getwindowgeometry', window_id], text=True).strip()
            size_line = [l for l in geometry.split('\n') if l.startswith('Geometry:')][0]
            size_parts = size_line.split(':')[1].strip().split('x')
            w_pixel = int(size_parts[0])
            h_pixel = int(size_parts[1])
            char_w = w_pixel // self.width
            char_h = h_pixel // self.height
            return max(8, char_w), max(16, char_h)
        except Exception:
            return 8, 16

    def __updateScreenInfo(self):
        time.sleep(0.2)
        self.x_screen, self.y_screen = self.__get_window_position_xdotool()
        self.char_width_pixel, self.char_height_pixel = self.__get_char_size()

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getScreenPosition(self):
        return self.x_screen, self.y_screen

    def getCharSize(self):
        return self.char_width_pixel, self.char_height_pixel