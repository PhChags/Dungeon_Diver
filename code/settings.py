# game setup
WIDTH    = 1280;
HEIGTH   = 720;
FPS      = 60;
TILESIZE = 64;
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0};

#ui 
BAR_HEIGHT = 20;
HEALTH_BAR_WIDTH = 200;
ENERGY_BAR_WIDTH = 140;
ITEM_BOX_SIZE = 80;
UI_FONT = 'assets/font/joystix.ttf';
UI_FONT_SIZE = 18;

#cores gerais
WATER_COLOR = '#71ddee';
UI_BG_COLOR = '#222222';
UPGRADE_BG_COLOR_SELECTED = '#333333';
UI_BORDER_COLOR = '#111111';
TEXT_COLOR = '#EEEEEE';
TEXT_COLOR_SELECTED = '#FFFFFF';
BAR_COLOR_SELECTED = '#124124';
BAR_COLOR = '#122122';

#cores ui
HEALTH_COLOR = 'red';
ENERGY_COLOR = 'blue';
UI_BORDER_COLOR_ACTIVE = 'gold';

#armas
weapon_data = {'sword': {'cooldown': 100, 'damage': 15,'graphic':'assets/weapons/sword/full.png'}};
	

#magias
magic_data = {'heal' : {'strength': 20,'cost': 10,'graphic':'assets/particles/heal/heal.png'}};

#inimigos
monster_data = {
	'squid': {'health': 100,'points':2500,'damage':20,'attack_type': 'slash', 'attack_sound':'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'points':5000,'damage':40,'attack_type': 'claw',  'attack_sound':'audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'points':1500,'damage':8,'attack_type': 'thunder', 'attack_sound':'audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'points':1000,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}};
