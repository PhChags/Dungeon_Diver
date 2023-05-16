from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.mouse import *

#inicializações tela
screen = Window(1224, 720);
mouse = Window.get_mouse();

background = GameImage("Assets/backgrounds/sky1.png");

def ranking():
    #inicializando a logo rank encima da tela
    rank = Sprite("Assets/ranking/ranklogo.png");
    rank.set_position(screen.width/2 - rank.width/2, screen.height/16);

    #inicializando o botão: retorna para o jogo
    retrn = Sprite("Assets/ranking/rtrn.png");
    retrn.set_position(screen.width - retrn.width, screen.height - screen.height/16);

    retrnpink = Sprite("Assets/ranking/pinkretrn.png");
    retrnpink.set_position(screen.width - retrnpink.width, screen.height - screen.height/16);

    #GameLoop
    while True:
        background.draw();

    #botao retorna
        if (mouse.is_over_object(retrn)):
            retrn.hide();
            retrnpink.draw();
            if (mouse.is_button_pressed(1)):
                return False;
        else:
            retrn.unhide();
        
        rank.draw();
        retrn.draw();
        screen.update();

