from __future__ import annotations

from typing import Optional

from vendor.pplay.window import Window


class Scene:
    _window: Optional[Window]

    def __init__(self):
        self._window = None
        self._manager = None

    def is_overlay(self) -> bool:
        return False

    def is_detached(self) -> bool:
        return self._window is None

    def attach_to_window(self, window: Window, manager):
        self._window = window
        self._manager = manager
        self.did_attach_to_window(window)

    def detach_from_window(self):
        self._window = None

    def did_attach_to_window(self, window: Window):
        return

    def get_window(self):
        return self._window

    def end(self):
        self._manager.end_scene(self)

    def show(self, scene: Scene):
        self._manager.show_scene(scene)

    def draw(self):
        self._window.update()
