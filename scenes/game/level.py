import pygame

from core.scene import Scene
from core.asset import *

from .pause import Pause


class Level(Scene):
    _pause = Pause()

    def draw(self):
        _background = resolve_game_image("backgrounds/sky1.png")
        _background.draw()

        window = self.get_window()
        if window is not None:
            if window.get_keyboard().key_up(pygame.K_ESCAPE):
                super().show(self._pause)
                return

        if self._pause.did_press_quit():
            super().end()
            return

        super().draw()
