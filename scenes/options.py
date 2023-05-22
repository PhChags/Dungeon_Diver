from core.scene import Scene
from core.ui import UIButton, UISwitch
from core.layout import *
from core.asset import resolve_game_image


class Options(Scene):
    _window_padding = 64

    _background = resolve_game_image("backgrounds/sky1.png")
    _title = resolve_game_image("options/logoopt.png")

    _back = UIButton(
        resolve_game_image("options/rtrn.png"),
        resolve_game_image("options/pinkretrn.png"),
    )

    _music = resolve_game_image("options/msc.png")
    _sound = resolve_game_image("options/sound.png")

    _music_switches = dict(
        on=UISwitch(
            on=resolve_game_image("options/greenyes.png"),
            off=resolve_game_image("options/blueyes.png"),
            state=True,
        ),
        off=UISwitch(
            on=resolve_game_image("options/greenno.png"),
            off=resolve_game_image("options/blueno.png"),
            state=False,
        ),
    )

    _sound_switches = dict(
        on=UISwitch(
            on=resolve_game_image("options/greenyes.png"),
            off=resolve_game_image("options/blueyes.png"),
            state=True,
        ),
        off=UISwitch(
            on=resolve_game_image("options/greenno.png"),
            off=resolve_game_image("options/blueno.png"),
            state=False,
        ),
    )

    def did_attach_to_window(self, window: Window):
        mouse = window.get_mouse()

        self._back.set_mouse(mouse)

        for switch in self._music_switches.values():
            switch.set_mouse(mouse)

        for switch in self._sound_switches.values():
            switch.set_mouse(mouse)

        self._layout_items(window)

    def draw(self):
        self._background.draw()
        self._title.draw()

        self._music.draw()
        self._draw_switches(self._music_switches)

        self._sound.draw()
        self._draw_switches(self._sound_switches)

        self._back.draw()
        if self._back.did_press():
            super().end()
            return

        super().draw()

    def _draw_switches(self, switches: dict[str, UISwitch]):
        for value, switch in switches.items():
            opposite_value = "off" if value == "on" else "on"
            opposite_switch = switches[opposite_value]

            if switch.did_press():
                switch.set(True)
                opposite_switch.set(False)

            switch.draw()

    def _layout_items(self, window: Window):
        center_in_window(self._background, window)

        center_x_in_window(self._title, window)
        self._title.y = self._window_padding

        self._music.set_position(408, 298)
        self._sound.set_position(672, 298)

        self._music_switches["off"].set_position(432, 362)
        self._music_switches["on"].set_position(524, 362)

        self._sound_switches["off"].set_position(696, 362)
        self._sound_switches["on"].set_position(788, 362)

        center_x_in_window(self._back, window)
        self._back.y = window.height - self._back.height - self._window_padding
