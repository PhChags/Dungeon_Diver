import pygame, sys
from settings import *
from level import Level

def game():
	#setup geral
	pygame.init();
	screen = pygame.display.set_mode((WIDTH,HEIGTH));
	pygame.display.set_caption('Dungeon Diver');
	clock = pygame.time.Clock();

	level = Level();

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();
				sys.exit();
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					level.toggle_menu();

		screen.fill(WATER_COLOR);
		a = level.run();
		pygame.display.update();
		clock.tick(FPS);

		if a == 0:
			return a;