from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *

#inicializações
screen = Window(1224, 822);
mouse = Window.get_mouse();

#função options
def options ():
    #colocando o logo options encima da tela
    options = Sprite("Assets/options/optlg.png");
    options.x = screen.width / 2 - options.width / 2;
    options.y = screen.height / 10;

    #inicializando o botão: retorna para o jogo
    retrn = Sprite("Assets/options/rtrn.png");
    retrn.x = screen.width / 2 - retrn.width / 2;
    retrn.y = screen.height /2 + 120;

    retrnred = Sprite("Assets/options/rtrnred.png");
    retrnred.x = screen.width / 2 - retrnred.width / 2;
    retrnred.y = screen.height /2 + 120;

    #inicializando o botão: opções
    som = Sprite("Assets/options/som.png");
    som.x = screen.width / 2 - som.width / 2;
    som.y = screen.height /2 - 120;

    #somred = Sprite("Assets/options/somred.png");
    #somred.x = screen.width / 2 - somred.width / 2;
    #somred.y = screen.height /2;

    #inicializando o botão: sair (que leva ao menu principal)
    music = Sprite("Assets/options/music.png");
    music.x = screen.width / 2 - music.width / 2;
    music.y = screen.height /2;

    #musicred = Sprite("Assets/options/musicred.png");
    #musicred.x = screen.width / 2 - musicred.width / 2;
    #musicred.y = screen.height /2 + 60; fiz esses sprites, 
    #mas apenas agora percebi que não devemos utiliza-los, pois haverá um botão com um altofalante com som e um mutado para representar com ou sem som e uma "sinfonia" e uma sinfonia riscada para representar com ou sem música

    #Game Loop
    while True:
        screen.set_background_color((0,0,0));

        if (mouse.is_over_object(retrn)):
            retrn.hide();
            retrnred.draw();
            if (mouse.is_button_pressed(1)):
                return False;
        else:
            retrn.unhide();
        
        options.draw();
        retrn.draw();
        music.draw();
        som.draw();
        screen.update();