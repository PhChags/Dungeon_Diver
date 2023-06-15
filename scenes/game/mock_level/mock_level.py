from core.asset import resolve_sprite
from core.layout import center_in_window
from core.scene import Scene

from .world import MockLevelWorld


class MockLevel(Scene):
    _world = MockLevelWorld()
    _player = resolve_sprite("characters/player.png")

    def __init__(self):
        super().__init__()
        self._player.set_curr_frame(0)

    def draw(self):
        self._world.draw()

        if self.get_window() is not None:
            center_in_window(self._player, self.get_window())
            self._player.draw()

        super().draw()
