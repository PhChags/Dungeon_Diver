from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import * 
from PPlay.gameimage import *
from ranking import ranking

#Inicializações
def menu():
    screen = Window(1280, 720); #não necessariamente configuração final 
    screen.set_title("Dungeon Diver");

    background = GameImage("assets/menus/background.png");

    mouse = Window.get_mouse();

    logo = Sprite("assets/menus/menu/logo.png");
    logo.set_position(screen.width/2 - logo.width/2, screen.height/16);

    start = Sprite("assets/menus/menu/start.png");
    start.set_position(screen.width/2 - start.width/2, screen.height/1.325);

    startpink = Sprite("assets/menus/menu/pinkstart.png");
    startpink.set_position(screen.width/2 - startpink.width/2, screen.height/1.325);

    rank = Sprite("assets/menus/menu/rank.png");
    rank.set_position(screen.width/2 - rank.width/2, screen.height/1.215);

    rankpink = Sprite("assets/menus/menu/pinkrank.png");
    rankpink.set_position(screen.width/2 - rankpink.width/2, screen.height/1.215);

    qut = Sprite("assets/menus/menu/quit.png");
    qut.set_position(screen.width/2 - qut.width/2, screen.height/1.125);

    qutpink = Sprite("assets/menus/menu/pinkquit.png");
    qutpink.set_position(screen.width/2 - qut.width/2, screen.height/1.125);

    click = 0;

    #Game Loop
    while True:
        background.draw();
        click += screen.delta_time();

        if (mouse.is_over_object(start)):
            start.hide();
            startpink.draw();
            if (mouse.is_button_pressed(1)) and click > 2:
                return 1;
        else:
            start.unhide();

        if (mouse.is_over_object(rank)):
            rank.hide();
            rankpink.draw();
            if (mouse.is_button_pressed(1)) and click > 2:
               return 2;
                   
                
        else:
            rank.unhide();

        if (mouse.is_over_object(qut)):
            qut.hide();
            qutpink.draw();
            if (mouse.is_button_pressed(1)) and click > 7: 
                exit();
        else:
            qut.unhide();

        logo.draw();
        start.draw();
        rank.draw();
        qut.draw();
        screen.update();
