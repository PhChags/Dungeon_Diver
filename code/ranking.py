from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.mouse import *
from settings import *

#inicializações tela
screen = Window(1280, 720);
mouse = Window.get_mouse();

background = GameImage("assets/menus/background.png");

def ranking():
    #inicializando a logo rank encima da tela
    rank = Sprite("assets/menus/ranking/ranklogo.png");
    rank.set_position(screen.width/2 - rank.width/2, screen.height/16);

    #inicializando o botão: retorna para o jogo
    retrn = Sprite("assets/menus/ranking/rtrn.png");
    retrn.set_position(screen.width/2 - retrn.width/2, screen.height - screen.height/16);

    retrnpink = Sprite("assets/menus/ranking/pinkretrn.png");
    retrnpink.set_position(screen.width/2 - retrnpink.width/2, screen.height - screen.height/16);

    #GameLoop
    while True:
        background.draw();

    #botao retorna
        if (mouse.is_over_object(retrn)):
            retrn.hide();
            retrnpink.draw();
            if (mouse.is_button_pressed(1)):
                return 0;
        else:
            retrn.unhide();
        
        with open("ranking.txt", "r") as r:
            players = r.readlines();
            size = len(players);
            if size > 7: size = 7;

            for p in range(size):
                players[p] = players[p].split(" - ");
                players[p][1] = int(players[p][1][:-1]);
            
            players = sorted(players, key=lambda player: player[1], reverse=True);
            for p in range(size):
                screen.draw_text(f"{p+1}. {players[p][0]} - {players[p][1]}", screen.width/2.3, 200+60*p, size=40, color=(240,240,240), font_name=UI_FONT);
        
        rank.draw();
        retrn.draw();
        screen.update();

