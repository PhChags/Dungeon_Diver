# Essa classe será constituída por uma função, função essa que será chamada pela classe jogo quando o jogador pressionar a tecla "ESC"
# se quiser visualizar a interface, basta chamar a função pause na classe menu
from vendor.pplay.window import *
from vendor.pplay.sprite import *
from vendor.pplay.mouse import *
from vendor.pplay.gameimage import *
from options import options

from core.asset import *

# inicializações
screen = Window(1224, 720)
mouse = Window.get_mouse()

background = resolve_game_image("backgrounds/sky1.png")


# função pause
def pause():
    # colocando o logo pause encima da tela
    pausar = resolve_sprite("pause/pauselg.png")
    pausar.set_position(screen.width / 2 - pausar.width / 2, screen.height / 16)

    # inicializando o botão: retorna para o jogo
    retrn = resolve_sprite("pause/rtrn.png")
    retrn.set_position(screen.width / 2 - retrn.width / 2, screen.height / 1.31)

    retrnpink = resolve_sprite("pause/pinkretrn.png")
    retrnpink.set_position(screen.width / 2 - retrnpink.width / 2, screen.height / 1.31)

    # inicializando o botão: opções
    opt = resolve_sprite("pause/opt.png")
    opt.set_position(screen.width / 2 - opt.width / 2, screen.height / 1.21)

    optpink = resolve_sprite("pause/pinkopt.png")
    optpink.set_position(screen.width / 2 - opt.width / 2, screen.height / 1.21)

    # inicializando o botão: sair (que leva ao menu principal)
    qt = resolve_sprite("pause/quit.png")
    qt.set_position(screen.width / 2 - qt.width / 2, screen.height / 1.125)

    qtpink = resolve_sprite("pause/pinkquit.png")
    qtpink.set_position(screen.width / 2 - qt.width / 2, screen.height / 1.125)

    # Game Loop
    while True:
        background.draw()

        # botão quit
        if mouse.is_over_object(qt):
            qt.hide()
            qtpink.draw()
            if mouse.is_button_pressed(1):
                return True
        else:
            qt.unhide()

        # botão opções
        if mouse.is_over_object(opt):
            opt.hide()
            optpink.draw()
            if mouse.is_button_pressed(1):
                options()
        else:
            opt.unhide()

        # botao retorna
        if mouse.is_over_object(retrn):
            retrn.hide()
            retrnpink.draw()
            if mouse.is_button_pressed(1):
                return False
        else:
            retrn.unhide()

        pausar.draw()
        retrn.draw()
        opt.draw()
        qt.draw()
        screen.update()
