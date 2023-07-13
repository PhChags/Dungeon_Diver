from PPlay.window import *
from menu import menu
from game import game
from ranking import ranking

#setup 
screen = Window(1280,720);
screen.set_title("Dungeon Diver");

STATE = 0;

#som
main_sound = pygame.mixer.Sound('audio/main.ogg');
main_sound.set_volume(0.5);
main_sound.play(loops = -1);

#game loop
while True:
    if STATE == 0:
        STATE = menu();
    if STATE == 1:
        STATE = game();
    if STATE == 2:
        STATE = ranking();
    if STATE == 3:
        STATE = exit();