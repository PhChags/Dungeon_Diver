from settings import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.sprite import *

janela = Window(WIDTH, HEIGTH);
janela.set_title("Dungeon Diver");
mouse = mouse = Window.get_mouse();

def game_over(points):
    bk = GameImage('assets/menus/gameover/gameover.jpg');

    logo = Sprite("assets/menus/gameover/game_over.png");
    logo.set_position(janela.width/2 - logo.width/2, janela.height/16);

    return save_name(points, "YOU WERE NOT ABLE TO FREE THE ERLHYU FROM THE CURSE", logo, bk);
                
        
def win_screen(points):
    bk = GameImage('assets/menus/gameover/winscreen.jpg');
    logo = Sprite("assets/menus/gameover/the_end.png");
    logo.set_position(janela.width/2 - logo.width/2, janela.height/16);
    return save_name(points, "YOU WERE ABLE TO FREE THE ERLHYUNIANS FROM THE CURSE", logo, bk);

def save_name(points, text, logo, bk):
    background = bk;
    key = Window.get_keyboard();
    string = [];
    a = ["_", "_", "_"];
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
    b = 0;
    c = 0;
    ct = 0;
    cc = 0;
    qut = Sprite("assets/menus/gameover/quit.png");
    qut.set_position(janela.width/2 - qut.width/2, janela.height - janela.height/16);
    qutpink = Sprite("assets/menus/gameover/pinkquit.png");
    qutpink.set_position(janela.width/2 - qut.width/2, janela.height - janela.height/16);

    while True:
        #janela.set_background_color((0, 0 , 0));
        background.draw();
        logo.draw();
        janela.draw_text(text, janela.width/8 - 90, janela.height/4, size = 50, color = (240,240,240), font_name=UI_FONT);
        janela.draw_text("ENTER YOUR NICKNAME", janela.width/2 - 200, janela.height/1.5, size = 50, color = (240,240,240), font_name=UI_FONT);

        if (mouse.is_over_object(qut)):
            qut.hide();
            qutpink.draw();
            if (mouse.is_button_pressed(1)):
                return 0;
        else:
            qut.unhide();
        
        for i in range(3):
                if (key.key_pressed("UP") and ct == 0):
                    ct += 1;
                    if c == 26:
                        c = 0;
                    a[b] = alfabeto[c]
                    c = c + 1;

                if (key.key_pressed("DOWN") and ct == 0):
                    ct += 1;
                    c = c - 1;
                    if c == -1:
                        c = 25;
                    a[b] = alfabeto[c];

                if (key.key_pressed("ENTER") and cc == 0 and a[b] != "_"):
                    cc += 1;
                    c = 0;
                    b += 1;

                if ct != 0:
                    ct += 1;
                    if ct == 100:
                        ct = 0;

                if cc != 0:
                    cc += 1;
                    if cc == 100:
                        cc = 0;
                janela.draw_text(a[i], janela.width / 2 - 90 + 70 * i + 1, janela.height/2, size=100, color=(255, 255, 255));
        #janela.draw_text("PUT YOUR NICK", janela.width / 2 - 90, janela.height/2, size=50, color=(255, 255, 255));

        if b == 3:
            string.append(a[0] + a[1] + a[2]);
            break;
        qut.draw();
        janela.update();

    with open("ranking.txt", "a") as n:
        newString = ' '.join(string);
        newString += f"  -  {(points)}\n";
        n.write(newString);
        return 0;