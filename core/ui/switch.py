from vendor.pplay.gameimage import GameImage

from .pressable import UIPressable


class UISwitch(UIPressable):
    _on: GameImage
    _off: GameImage
    _state = False

    def __init__(self, on: GameImage, off: GameImage, state=False):
        super().__init__(on)
        self._state = state
        self._on = on
        self._off = off

    @property
    def x(self):
        return self._on.x

    @x.setter
    def x(self, value: float):
        self._on.x = value
        self._off.x = value

    @property
    def y(self):
        return self._on.y

    @y.setter
    def y(self, value: float):
        self._on.y = value
        self._off.y = value

    def set_position(self, x: float, y: float):
        self.x = x
        self.y = y

    def switch(self):
        self._state = not self._state

    def set(self, state: bool):
        self._state = state

    def draw(self):
        super().draw()
        if self._state is True:
            self._on.draw()
        else:
            self._off.draw()
