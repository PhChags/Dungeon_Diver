from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import * #como já fiz umas semanas da matéria antes, já sei como pegar comandos do teclado e mouse utilizando o PPlay :P

#Inicializações
screen = Window(1224, 822); #não necessariamente configuração final 
screen.set_title("Dungeon Diver");

mouse = Window.get_mouse();

logo = Sprite("Assets/menu/logo.png");
logo.x = screen.width/2 - logo.width/2;
logo.y = 100;

start = Sprite("Assets/menu/strt.png");
start.x = screen.width/2 - start.width/2;
start.y = screen.height/1.58+50;

startred = Sprite("Assets/menu/strtred.png");
startred.x = screen.width/2 - startred.width/2;
startred.y = screen.height/1.58+50;

rank = Sprite("Assets/menu/rank.png");
rank.x = screen.width/2 - rank.width/2;
rank.y = screen.height/1.44+50;

rankred = Sprite("Assets/menu/rankred.png");
rankred.x = screen.width/2 - rankred.width/2;
rankred.y = screen.height/1.44+50;

opt = Sprite("Assets/menu/opt.png");
opt.x = screen.width/2 - opt.width/2;
opt.y = screen.height/1.32+50;

optred = Sprite("Assets/menu/optred.png");
optred.x = screen.width/2 - optred.width/2;
optred.y = screen.height/1.32+50;

qut = Sprite("Assets/menu/quit.png");
qut.x = screen.width/2 - qut.width/2.3;
qut.y = screen.height/1.22+50;

qutred = Sprite("Assets/menu/quitred.png");
qutred.x = screen.width/2 - qutred.width/2.3;
qutred.y = screen.height/1.22+50;
#os valores aleátorios colocados aqui (como 1.22), foram obtidos através de testes até que eu os considerasse ergonomicos; (sinta-se livre para modifica-los :P)

#Game Loop
while True:
    if (mouse.is_over_object(start)):
        start.hide();
        startred.draw();
        #if (mouse.is_button_pressed(1)): Nesse if aqui iniciamos o jogo :P
    else:
        start.unhide();

    if (mouse.is_over_object(rank)):
        rank.hide();
        rankred.draw();
        #if (mouse.is_button_pressed(1)): Já nesse mostramos a tela de rank
    else:
        rank.unhide();
    
    if (mouse.is_over_object(opt)):
        opt.hide();
        optred.draw();
        #if (mouse.is_button_pressed(1)): Nesse aqui mostramos a tela de opções (originalmente apenas com opção de tirar som e/ou musica)
    else:
        opt.unhide();

    if (mouse.is_over_object(qut)):
        qut.hide();
        qutred.draw();
        if (mouse.is_button_pressed(1)): #E nesse, que já está implementado, finalizamos o jogo
            break;
    else:
        qut.unhide();

    logo.draw();
    start.draw();
    rank.draw();
    opt.draw();
    qut.draw();
    screen.update();

#Achei essa fonte na internet, se quiser alterar, sinta-se a vontade; Fiz o menu mas não me importo muito com questões estéticas
#Ps: Achei uma sprite interessante de um coração e comitei nos assets