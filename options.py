from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *

#inicializações
screen = Window(1224, 720);
mouse = Window.get_mouse();

#função options
def options ():
    #colocando o logo options encima da tela
    options = Sprite("Assets/options/logoopt.png");
    options.set_position(screen.width/2 - options.width/2, screen.height/16);

    #inicializando o botão: retorna para o jogo
    retrn = Sprite("Assets/options/rtrn.png");
    retrn.set_position(screen.width - retrn.width, screen.height - screen.height/16);

    retrnpink = Sprite("Assets/options/pinkretrn.png");
    retrnpink.set_position(screen.width - retrn.width, screen.height - screen.height/16);

    #inicializando escritos som e musica
    song = Sprite("Assets/options/sng.png");
    song.set_position(screen.width/2 - song.width/2, screen.height/2 - screen.height/8);

    music = Sprite("Assets/options/msc.png");
    music.set_position(screen.width/2 - music.width/2, screen.height/2 + screen.height/8);

    #Game Loop
    while True:
        screen.set_background_color((0,0,0));

        if (mouse.is_over_object(retrn)):
            retrn.hide();
            retrnpink.draw();
            if (mouse.is_button_pressed(1)):
                return False;
        else:
            retrn.unhide();
        
        options.draw();
        retrn.draw();
        music.draw();
        song.draw();
        screen.update();