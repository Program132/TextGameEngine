import pyautogui
import threading
import time
from src.Utils.TerminalWindow import TerminalWindow
from pynput import mouse


class MouseTracker:
    def __init__(self, term: TerminalWindow):
        self.term = term
        self.mouse_x = 0
        self.mouse_y = 0
        self._running = False
        self._thread = None
        self._listener = None
        self._on_left_click_handler = None
        self._on_right_click_handler = None

    def on_left_click(self, handler_function):
        self._on_left_click_handler = handler_function

    def on_right_click(self, handler_function):
        self._on_right_click_handler = handler_function

    def convert_screen_to_terminal_coords(self, x_screen, y_screen):
        x_term_screen, y_term_screen = self.term.getScreenPosition()
        char_w_pixel, char_h_pixel = self.term.getCharSize()

        x_relative_pixel = x_screen - x_term_screen
        y_relative_pixel = y_screen - y_term_screen

        x_terminal = max(0, x_relative_pixel // char_w_pixel)
        y_terminal = max(0, y_relative_pixel // char_h_pixel)

        x_terminal = min(x_terminal, self.term.getWidth() - 1)
        y_terminal = min(y_terminal, self.term.getHeight() - 1)

        return x_terminal, y_terminal

    def _on_click_event(self, x_screen, y_screen, button, pressed):
        if pressed:
            x_term, y_term = self.convert_screen_to_terminal_coords(x_screen, y_screen)
            is_inside = (
                0 <= x_term < self.term.getWidth() and
                0 <= y_term < self.term.getHeight()
            )
            if is_inside:
                if button == mouse.Button.left and self._on_left_click_handler:
                    self._on_left_click_handler(x_term, y_term)
                elif button == mouse.Button.right and self._on_right_click_handler:
                    self._on_right_click_handler(x_term, y_term)

    def _update_loop(self):
        while self._running:
            x_screen, y_screen = pyautogui.position()
            self.mouse_x, self.mouse_y = self.convert_screen_to_terminal_coords(x_screen, y_screen)
            time.sleep(0.05)

    def start(self):
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._update_loop, daemon=True)
            self._thread.start()

            self._listener = mouse.Listener(on_click=self._on_click_event)
            self._listener.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join()
        if self._listener:
            self._listener.stop()

    def get_terminal_position(self):
        return self.mouse_x, self.mouse_y
        