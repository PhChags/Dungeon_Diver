from vendor.pplay.gameimage import GameImage

from .pressable import UIPressable


class UIButton(UIPressable):
    _normal: GameImage
    _focused: GameImage

    def __init__(self, normal: GameImage, focused: GameImage):
        super().__init__(normal)
        self._normal = normal
        self._focused = focused

    @property
    def x(self):
        return self._normal.x

    @x.setter
    def x(self, value: float):
        self._normal.x = value
        self._focused.x = value

    @property
    def y(self):
        return self._normal.y

    @y.setter
    def y(self, value: float):
        self._normal.y = value
        self._focused.y = value

    @property
    def width(self):
        return self._normal.width

    @width.setter
    def width(self, value: int):
        self._normal.width = value
        self._focused.width = value

    @property
    def height(self):
        return self._normal.height

    @height.setter
    def height(self, value: int):
        self._normal.height = value
        self._focused.height = value

    def set_position(self, x: float, y: float):
        self.x = x
        self.y = y

    def draw(self):
        super().draw()
        if self.did_focus():
            self._focused.draw()
        else:
            self._normal.draw()
