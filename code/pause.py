from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.gameimage import *

#setup
screen = Window(1280, 720);
mouse = Window.get_mouse();

background = GameImage("assets/menus/background.png");

#função pause
def pause ():
    #colocando o logo pause encima da tela
    pausar = Sprite("assets/menus/pause/pauselg.png");
    pausar.set_position(screen.width/2 - pausar.width/2, screen.height/16);

    #inicializando o botão: retorna para o jogo
    retrn = Sprite("assets/menus/pause/rtrn.png");
    retrn.set_position(screen.width/2 - retrn.width/2, screen.height/1.15);

    retrnpink = Sprite("assets/menus/pause/pinkretrn.png");
    retrnpink.set_position(screen.width/2 - retrnpink.width/2, screen.height/1.15);

    qt = Sprite("assets/menus/pause/quit.png");
    qt.set_position(screen.width/2 - qt.width/2, screen.height - screen.height/16);

    qtpink = Sprite("assets/menus/pause/pinkquit.png");
    qtpink.set_position(screen.width/2 - qt.width/2, screen.height - screen.height/16);

    #Game Loop
    while True:
        background.draw();

    #botão quit
        if (mouse.is_over_object(qt)):
            qt.hide();
            qtpink.draw();
            if (mouse.is_button_pressed(1)):
                return 0;
        else:
            qt.unhide();

    #botao retorna
        if (mouse.is_over_object(retrn)):
            retrn.hide();
            retrnpink.draw();
            if (mouse.is_button_pressed(1)):
                return 1;
        else:
            retrn.unhide();
        
        pausar.draw();
        retrn.draw();
        qt.draw();
        screen.update();