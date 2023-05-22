import pygame

from core.asset import *
from core.layout import *
from core.ui import UIButton
from core.scene import Scene

from ..options import Options


class Pause(Scene):
    _did_skip_tick = False
    _did_press_quit = False

    _window_padding = 64
    _buttons_spacing = 24

    _background = resolve_game_image("backgrounds/sky1.png")
    _title = resolve_game_image("pause/pauselg.png")

    _buttons = {
        "quit": UIButton(resolve_game_image("menu/quit.png"), resolve_game_image("menu/pinkquit.png")),
        "options": UIButton(resolve_game_image("pause/opt.png"), resolve_game_image("pause/pinkopt.png")),
        "return": UIButton(
            resolve_game_image("pause/rtrn.png"),
            resolve_game_image("pause/pinkretrn.png"),
        ),
    }

    def did_attach_to_window(self, window: Window):
        self._did_press_quit = False
        self._did_skip_tick = False

        for btn in self._buttons.values():
            btn.set_mouse(window.get_mouse())
        self._layout_items(window)

    def did_press_quit(self):
        return self._did_press_quit

    def draw(self):
        self._background.draw()
        self._title.draw()

        for btn in self._buttons.values():
            btn.draw()

        if self._buttons["return"].did_press():
            super().end()
            return

        if self._buttons["quit"].did_press():
            self._did_press_quit = True
            super().end()
            return

        if self._buttons["options"].did_press():
            super().show(Options())
            return

        window = self.get_window()
        if window is not None and self._did_skip_tick:
            if window.get_keyboard().key_up(pygame.K_ESCAPE):
                super().end()
                return

        self._did_skip_tick = True
        super().draw()

    def _layout_items(self, window: Window):
        center_in_window(self._background, window)

        center_x_in_window(self._title, window)
        self._title.y = self._window_padding

        buttons_col = list(reversed(self._buttons.values()))
        for idx, btn in enumerate(buttons_col):
            anchor_y = window.height if idx == 0 else buttons_col[idx - 1].y
            spacing_y = self._window_padding if idx == 0 else self._buttons_spacing
            btn.y = anchor_y - spacing_y - btn.height
            center_x_in_window(btn, window)
