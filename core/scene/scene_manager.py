from typing import Callable

from vendor.pplay.window import Window

from .scene import Scene


class SceneManager:
    _scenes: list[Scene] = []
    _window: Window

    def __init__(self, window: Window):
        self._window = window

    def has_no_scenes_to_show(self):
        return len(self._scenes) == 0

    def show_scene(self, scene: Scene):
        current_scene = self.get_current_scene()
        if current_scene is not None and not current_scene.is_overlay():
            current_scene.detach_from_window()

        self._scenes.append(scene)
        scene.attach_to_window(self._window, self)

    def end_scene(self, scene: Scene):
        try:
            scene_idx = self._scenes.index(scene)

            self._scenes[scene_idx].detach_from_window()
            if scene_idx == len(self._scenes) - 1:
                self._scenes[scene_idx - 1].attach_to_window(self._window, self)

            del self._scenes[scene_idx]
        except ValueError:
            return

    def end_current_scene(self):
        current_scene = self.get_current_scene()
        if current_scene is None:
            return

        self.end_scene(current_scene)

    def get_current_scene(self):
        if len(self._scenes) == 0:
            return None

        return self._scenes[len(self._scenes) - 1]

    def tick(self):
        if self.get_current_scene().is_detached():
            return

        self.get_current_scene().draw()
