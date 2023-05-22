from vendor.pplay.window import Window

from core.asset import *
from core.layout import *
from core.scene import Scene
from core.ui import UIButton

from .ranking import Ranking
from .options import Options
from .game import Level


class MainMenu(Scene):
    _window_padding = 64
    _buttons_spacing = 24

    _background = resolve_game_image("backgrounds/sky1.png")
    _logo = resolve_sprite("menu/logo.png")

    _buttons = dict(
        start=UIButton(
            resolve_game_image("menu/start.png"),
            resolve_game_image("menu/pinkstart.png"),
        ),
        rank=UIButton(resolve_game_image("menu/rank.png"), resolve_game_image("menu/pinkrank.png")),
        options=UIButton(resolve_game_image("menu/opt.png"), resolve_game_image("menu/pinkopt.png")),
        quit=UIButton(resolve_game_image("menu/quit.png"), resolve_game_image("menu/pinkquit.png")),
    )

    def did_attach_to_window(self, window: Window):
        mouse = window.get_mouse()
        for btn in self._buttons.values():
            btn.set_mouse(mouse)
        self._layout_items(window)

    def draw(self):
        self._background.draw()
        self._logo.draw()

        for btn in self._buttons.values():
            btn.draw()

        if self._buttons["start"].did_press():
            super().show(Level())
            return

        if self._buttons["rank"].did_press():
            super().show(Ranking())
            return

        if self._buttons["options"].did_press():
            super().show(Options())
            return

        if self._buttons["quit"].did_press():
            super().end()
            return

        super().draw()
        return

    def _layout_items(self, window: Window):
        center_in_window(self._background, window)

        self._logo.y = self._window_padding
        center_x_in_window(self._logo, window)

        buttons_col = list(reversed(self._buttons.values()))
        for idx, btn in enumerate(buttons_col):
            anchor_y = window.height if idx == 0 else buttons_col[idx - 1].y
            spacing_y = self._window_padding if idx == 0 else self._buttons_spacing
            btn.y = anchor_y - spacing_y - btn.height
            center_x_in_window(btn, window)
