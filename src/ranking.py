from vendor.pplay.window import *
from vendor.pplay.gameimage import *
from vendor.pplay.sprite import *
from vendor.pplay.mouse import *

# inicializações tela
screen = Window(1224, 720)
mouse = Window.get_mouse()

background = GameImage("../assets/backgrounds/sky1.png")


def ranking():
    # inicializando a logo rank encima da tela
    rank = Sprite("../assets/ranking/ranklogo.png")
    rank.set_position(screen.width / 2 - rank.width / 2, screen.height / 16)

    # inicializando o botão: retorna para o jogo
    retrn = Sprite("../assets/ranking/rtrn.png")
    retrn.set_position(screen.width - retrn.width, screen.height - screen.height / 16)

    retrnpink = Sprite("../assets/ranking/pinkretrn.png")
    retrnpink.set_position(screen.width - retrnpink.width, screen.height - screen.height / 16)

    # GameLoop
    while True:
        background.draw()

        # botao retorna
        if mouse.is_over_object(retrn):
            retrn.hide()
            retrnpink.draw()
            if mouse.is_button_pressed(1):
                return False
        else:
            retrn.unhide()

        rank.draw()
        retrn.draw()
        screen.update()
