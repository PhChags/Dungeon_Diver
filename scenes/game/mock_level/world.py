from core.asset import resolve_sprite


class MockLevelWorld:
    _sprite = resolve_sprite("world/world1.png")

    def draw(self):
        self._sprite.x = 0
        self._sprite.y = 0
        self._sprite.draw()
