from core.layout import *
from core.ui import UIButton
from core.asset import resolve_sprite, resolve_game_image
from core.scene import Scene


class Ranking(Scene):
    _window_padding = 64

    _background = resolve_game_image("backgrounds/sky1.png")
    _title = resolve_sprite("ranking/ranklogo.png")

    _back = UIButton(
        resolve_game_image("ranking/rtrn.png"),
        resolve_game_image("ranking/pinkretrn.png"),
    )

    def did_attach_to_window(self, window: Window):
        self._back.set_mouse(window.get_mouse())
        self._layout_items(window)

    def draw(self):
        self._background.draw()
        self._title.draw()

        self._back.draw()
        if self._back.did_press():
            super().end()
            return

        super().draw()

    def _layout_items(self, window: Window):
        center_in_window(self._background, window)

        center_x_in_window(self._title, window)
        self._title.y = self._window_padding

        center_x_in_window(self._back, window)
        self._back.y = window.height - self._back.height - self._window_padding
