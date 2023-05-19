from vendor.pplay.window import *
from vendor.pplay.sprite import *
from vendor.pplay.mouse import *  # como já fiz umas semanas da matéria antes, já sei como pegar comandos do teclado e mouse utilizando o PPlay :P
from vendor.pplay.gameimage import *

from core.asset import *

from options import options
from ranking import ranking
from game import (
    game,
)  # caso queira vizualizar a interface da classe pause, atualmente a classe game só chama a classe pause ao teclar "ESC"

# Inicializações
screen = Window(1224, 720)
# não necessariamente configuração final
screen.set_title("Dungeon Diver")

background = resolve_game_image("backgrounds/sky1.png")

mouse = Window.get_mouse()

logo = resolve_sprite("menu/logo.png")
logo.set_position(screen.width / 2 - logo.width / 2, screen.height / 16)

start = resolve_sprite("menu/start.png")
start.set_position(screen.width / 2 - start.width / 2, screen.height / 1.42)

startpink = resolve_sprite("menu/pinkstart.png")
startpink.set_position(screen.width / 2 - startpink.width / 2, screen.height / 1.42)

rank = resolve_sprite("menu/rank.png")
rank.set_position(screen.width / 2 - rank.width / 2, screen.height / 1.31)

rankpink = resolve_sprite("menu/pinkrank.png")
rankpink.set_position(screen.width / 2 - rankpink.width / 2, screen.height / 1.31)

opt = resolve_sprite("menu/opt.png")
opt.set_position(screen.width / 2 - opt.width / 2, screen.height / 1.21)

optpink = resolve_sprite("menu/pinkopt.png")
optpink.set_position(screen.width / 2 - opt.width / 2, screen.height / 1.21)

qut = resolve_sprite("menu/quit.png")
qut.set_position(screen.width / 2 - qut.width / 2, screen.height / 1.125)

qutpink = resolve_sprite("menu/pinkquit.png")
qutpink.set_position(screen.width / 2 - qut.width / 2, screen.height / 1.125)
# os valores aleátorios colocados aqui (como 1.22), foram obtidos através de testes até que eu os considerasse ergonomicos; (sinta-se livre para modifica-los :P)

# Game Loop
while True:
    background.draw()

    if mouse.is_over_object(start):
        start.hide()
        startpink.draw()
        if mouse.is_button_pressed(1):  # Nesse if aqui iniciamos o jogo :P
            game()
    else:
        start.unhide()

    if mouse.is_over_object(rank):
        rank.hide()
        rankpink.draw()
        if mouse.is_button_pressed(1):  # Já nesse mostramos a tela de rank
            ranking()
    else:
        rank.unhide()

    if mouse.is_over_object(opt):
        opt.hide()
        optpink.draw()
        if mouse.is_button_pressed(
            1
        ):  # Nesse aqui mostramos a tela de opções (originalmente apenas com opção de tirar som e/ou musica)
            options()
    else:
        opt.unhide()

    if mouse.is_over_object(qut):
        qut.hide()
        qutpink.draw()
        if mouse.is_button_pressed(1):  # E nesse, que já está implementado, finalizamos o jogo
            break
    else:
        qut.unhide()

    logo.draw()
    start.draw()
    rank.draw()
    opt.draw()
    qut.draw()
    screen.update()

# Achei essa fonte na internet, se quiser alterar, sinta-se a vontade; Fiz o menu mas não me importo muito com questões estéticas
# Ps: Achei uma sprite interessante de um coração e comitei nos assets
