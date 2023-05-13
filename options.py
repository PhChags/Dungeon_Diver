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

    #inicializando o botão: retorna para quem chamou a função
    retrn = Sprite("Assets/options/rtrn.png");
    retrn.set_position(screen.width - retrn.width, screen.height - screen.height/16);

    retrnpink = Sprite("Assets/options/pinkretrn.png");
    retrnpink.set_position(screen.width - retrn.width, screen.height - screen.height/16);

    #inicializando escritos som e musica
    sound = Sprite("Assets/options/sound.png");
    sound.set_position(screen.width/2 - sound.width/2, screen.height/2);

    music = Sprite("Assets/options/msc.png");
    music.set_position(screen.width/2 - music.width/2, screen.height/2 + screen.height/6);

    #inicializando os botões ativa/desativa som/musica
    s_click_off = False;
    s_click_on = True;
    m_click_off = False;
    m_click_on = True;

    s_botao_off_clicado = Sprite("Assets/options/greenno.png");
    s_botao_on_clicado = Sprite("Assets/options/greenyes.png");
    s_botao_off_clicado.set_position(screen.width/2 - s_botao_off_clicado.width/2 + screen.width/20, screen.height/2 + screen.height/16);
    s_botao_on_clicado.set_position(screen.width/2 - s_botao_on_clicado.width/2 - screen.width/20, screen.height/2 + screen.height/16);
    
    s_botao_off = Sprite("Assets/options/blueno.png");
    s_botao_on = Sprite("Assets/options/blueyes.png");
    s_botao_off.set_position(screen.width/2 - s_botao_off.width/2 + screen.width/20, screen.height/2 + screen.height/16);
    s_botao_on.set_position(screen.width/2 - s_botao_on.width/2 - screen.width/20, screen.height/2 + screen.height/16);

    m_botao_off_clicado = Sprite("Assets/options/greenno.png");
    m_botao_on_clicado = Sprite("Assets/options/greenyes.png");
    m_botao_off_clicado.set_position(screen.width/2 - m_botao_off_clicado.width/2 + screen.width/20, screen.height/2 + screen.height/4);
    m_botao_on_clicado.set_position(screen.width/2 - m_botao_on_clicado.width/2 - screen.width/20, screen.height/2 + screen.height/4);

    m_botao_off = Sprite("Assets/options/blueno.png");
    m_botao_on = Sprite("Assets/options/blueyes.png");
    m_botao_off.set_position(screen.width/2 - m_botao_off.width/2 + screen.width/20, screen.height/2 + screen.height/4);
    m_botao_on.set_position(screen.width/2 - m_botao_on.width/2 - screen.width/20, screen.height/2 + screen.height/4);

    #Game Loop
    while True:
        screen.set_background_color((0,0,0));

    #Ainda falta manter as configurações ativas para qunado o menu opções for aberto denovo
    #Mecanismo ativa/desativa som (apenas interface)
        if(s_click_on):
            if(mouse.is_over_object(s_botao_off_clicado)):
                if (mouse.is_button_pressed(1)):
                    s_click_off = True;
                    s_click_on = False;
        
        if(s_click_off):
            s_botao_off.hide();
            s_botao_off_clicado.draw();
            s_botao_on_clicado.hide();
            s_botao_on.draw();
        else:
            s_botao_off.unhide();
            s_botao_on_clicado.unhide();

        if(s_click_off):
            if(mouse.is_over_object(s_botao_on_clicado)):
                if (mouse.is_button_pressed(1)):
                    s_click_on = True;
                    s_click_off = False;
        
        if(s_click_on):
            s_botao_on.hide();
            s_botao_on_clicado.draw();
            s_botao_off_clicado.hide();
            s_botao_off.draw();
        else:
            s_botao_on.unhide();
            s_botao_off_clicado.unhide();
        
    #Mecanismo ativa/desativa musica (apenas interface)
        if(m_click_on):
            if(mouse.is_over_object(m_botao_off_clicado)):
                if (mouse.is_button_pressed(1)):
                    m_click_off = True;
                    m_click_on = False;
        
        if(m_click_off):
            m_botao_off.hide();
            m_botao_off_clicado.draw();
            m_botao_on_clicado.hide();
            m_botao_on.draw();
        else:
            m_botao_off.unhide();
            m_botao_on_clicado.unhide();

        if(m_click_off):
            if(mouse.is_over_object(m_botao_on_clicado)):
                if (mouse.is_button_pressed(1)):
                    m_click_on = True;
                    m_click_off = False;
        
        if(m_click_on):
            m_botao_on.hide();
            m_botao_on_clicado.draw();
            m_botao_off_clicado.hide();
            m_botao_off.draw();
        else:
            m_botao_on.unhide();
            m_botao_off_clicado.unhide();

    #botao retorna
        if (mouse.is_over_object(retrn)):
            retrn.hide();
            retrnpink.draw();
            if (mouse.is_button_pressed(1)):
                return False;
        else:
            retrn.unhide();
        
    #desenho de cena    
        options.draw();
        retrn.draw();
        music.draw();
        sound.draw();
        screen.update();