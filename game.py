from vendor.pplay.window import *
from vendor.pplay.gameimage import *
from vendor.pplay.sprite import *
from vendor.pplay.keyboard import *
from pause import pause

from core.asset import *

screen = Window(1224, 720)
keyboard = screen.get_keyboard()

background = resolve_game_image("backgrounds/sky1.png")


def game():
    while True:
        background.draw()

        if keyboard.key_pressed("ESC"):
            t = pause()
            if t:
                break

        screen.update()
