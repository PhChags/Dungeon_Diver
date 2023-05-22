from typing import Optional

from vendor.pplay.gameimage import GameImage
from vendor.pplay.mouse import Mouse


class UIPressable:
    _mouse: Optional[Mouse]
    _target: GameImage

    _did_focus = False
    _did_press = False
    _pressed = False

    def __init__(self, target: GameImage):
        self._target = target

    def set_mouse(self, mouse: Mouse):
        self._mouse = mouse

    def did_press(self):
        return self._did_press

    def did_focus(self):
        return self._did_focus

    def draw(self):
        if self._mouse is None:
            self._did_focus = False
            self._did_press = False
            return

        self._did_focus = self._mouse.is_over_object(self._target)
        self._did_press = self._did_focus and self._mouse.is_button_up(1)
