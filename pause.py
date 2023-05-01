#Essa classe será constituída por uma função, função essa que será chamada pela classe jogo quando o jogador pressionar a tecla "ESC"
#se quiser visualizar a interface, basta chamar a função pause na classe menu
from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from options import options

#inicializações
screen = Window(1224, 822);
mouse = Window.get_mouse();

#função pause
def pause ():
    #colocando o logo pause encima da tela
    pausar = Sprite("Assets/pause/pause.png");
    pausar.x = screen.width / 2 - pausar.width / 2;
    pausar.y = screen.height / 10;

    #inicializando o botão: retorna para o jogo
    retrn = Sprite("Assets/pause/rtrn.png");
    retrn.x = screen.width / 2 - retrn.width / 2;
    retrn.y = screen.height /2;

    retrnred = Sprite("Assets/pause/rtrnred.png");
    retrnred.x = screen.width / 2 - retrnred.width / 2;
    retrnred.y = screen.height /2;

    #inicializando o botão: opções
    opt = Sprite("Assets/pause/opt.png");
    opt.x = screen.width / 2 - opt.width / 2;
    opt.y = screen.height /2 + 60;

    optred = Sprite("Assets/pause/optred.png");
    optred.x = screen.width / 2 - optred.width / 2;
    optred.y = screen.height /2 + 60;

    #inicializando o botão: sair (que leva ao menu principal)
    qt = Sprite("Assets/pause/quit.png");
    qt.x = screen.width / 2 - qt.width / 2.3;
    qt.y = screen.height /2 + 120;

    qtred = Sprite("Assets/pause/quitred.png");
    qtred.x = screen.width / 2 - qtred.width / 2.3;
    qtred.y = screen.height /2 + 120;

    #Game Loop
    while True:
        screen.set_background_color((0,0,0));

        if (mouse.is_over_object(qt)):
            qt.hide();
            qtred.draw();
            if (mouse.is_button_pressed(1)):
                return True;
        else:
            qt.unhide();

        if (mouse.is_over_object(opt)):
            opt.hide();
            optred.draw();
            if (mouse.is_button_pressed(1)): 
                options();
        else:
            opt.unhide();

        if (mouse.is_over_object(retrn)):
            retrn.hide();
            retrnred.draw();
            if (mouse.is_button_pressed(1)):
                return False;
        else:
            retrn.unhide();
        
        pausar.draw();
        retrn.draw();
        opt.draw();
        qt.draw();
        screen.update();