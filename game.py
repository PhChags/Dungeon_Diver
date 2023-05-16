from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from pause import pause

screen = Window(1224, 720);
keyboard = screen.get_keyboard();

background = GameImage("Assets/backgrounds/sky1.png");

def game():
    while True:
        background.draw();

        if(keyboard.key_pressed("ESC")):
            t = pause();
            if t:
                break;

        screen.update();