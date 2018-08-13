
import sys
import pygame

from Settings import Settings
from Settings import Ship
from Settings import Allian
from bullet import Bullet
from game_stats import GameStats
from game_stats import Button
from game_stats import Scoreboard

from random import randint
from pygame.sprite import Group

clock = pygame.time.Clock()
from time import sleep
def get_numer_A(Settings,screen):
	Wscreen, Hscreen = pygame.display.get_surface().get_size()
	allian = Allian(Settings,screen)
	allianW,allianH =allian.rect.size
	A_number_x = (Wscreen-allianW*2)//(allianW*2)
	A_number_h = (Hscreen-allianH*2)//(allianH*2)
	return A_number_x,A_number_h,allianW,allianH


def creat_fleet(Settings,screen,alliens,stats):
	

	A_number_x,A_number_h,allianW,allianH = get_numer_A(Settings,screen)
	#print(A_number_x,A_number_h,allianW,allianH)
	for aliH in range(A_number_h+1):
		for aliW in range(A_number_x):
			allian = Allian(Settings,screen)
			
			allian.rect.x = allianW+2*allianW*aliW#+randint(-allianW,allianW)
			allian.rect.y = allianH+1*allianH*aliH+randint(-allianH,5)
			alliens.add(allian)
	

def refill_fleat(Settings,screen,alliens):
	if Settings.Max_allians>0:
		for aliW in range(randint(1,Settings.Difficulty)):
			allian = Allian(Settings,screen)			
			allian.rect.x = randint(200,1500)
			allian.rect.y = 0
			alliens.add(allian)
			Settings.Max_allians-=1

def ship_hit(Settings,bullets,allians,screen,ship,stats):
	if stats.ship_left>0:
		stats.ship_left-=1
		allians.empty()
		bullets.empty()
		Settings.Difficulty=1
		creat_fleet(Settings,screen,allians,stats)	
		ship.center()
		sleep(1)
	else:
		allians.empty()
		bullets.empty()
		ship.center()
		stats.game_active = False
	
def update_Allians(Settings,bullets,allians,screen,ship,stats):


	
	stats.ship_left=len(allians)+Settings.Max_allians
	if pygame.sprite.spritecollideany(ship,allians):
		ship_hit(Settings,bullets,allians,screen,ship,stats)


	for allian in range(len(allians)):	
		

		if allians.sprites()[allian].check_bottom():
			ship_hit(Settings,bullets,allians,screen,ship,stats)
		elif allians.sprites()[allian].check_edges():
			allians.sprites()[allian].direction*=-1
			RandAli=randint(0,len(allians)-1)
			print("Random ali: " ,RandAli)
			allians.sprites()[RandAli].move_foward()
			#allians.sprites()[randint(0,len(allians)-1)].move_foward()
			#allians.sprites()[randint(0,len(allians)-1)].Difficulty+=1

		allians.sprites()[allian].blitme()
		allians.sprites()[allian].update()
		

def update_bullets(Settings,bullets,allians,screen,stats):
	for bullet in bullets.sprites():
		bullet.creat_bullet()
		bullet.update_bullet()
		
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	#check for collisions and delete ojects !!!			
	#collisions = pygame.sprite.groupcollide(bullets,allians,True,True)
	if pygame.sprite.groupcollide(bullets,allians,True,True):
		print("hit")
		refill_fleat(Settings,screen,allians)		
		stats.points+=Settings.Difficulty*20
		#Settings.Difficulty+=1
			#print("Bullets ",len(bullets))

def fire_bullet(my_settings,screen,ourShip,bullets):
	if len(bullets)< my_settings.bullets_allow:
		print("fire")
		new_bullet = Bullet(my_settings,screen,ourShip)
		bullets.add(new_bullet)

def Keydown(event,ourShip,bullets,screen,my_settings,stats,allians):
	#print(ourShip.rect.x,ourShip.rect.y)
	if event.key == pygame.K_RIGHT:
		ourShip.move_right = True		
	elif event.key == pygame.K_LEFT:
		ourShip.move_left = True
	elif event.key == pygame.K_UP:
		ourShip.move_up = True
	elif event.key == pygame.K_DOWN:
		ourShip.move_down = True

	elif event.key == 97:#Make smaller with a
		
		ourShip.rect.w=ourShip.rect.w+20
		ourShip.rect.h=ourShip.rect.h+20
		#print(ourShip.rect.w)
		w=ourShip.rect.w
		h=ourShip.rect.h

		ourShip.image=pygame.transform.scale(ourShip.image, (w, h))		

	elif event.key == 98:#Make bigger with b
		
		ourShip.rect.w=ourShip.rect.w-20
		ourShip.rect.h=ourShip.rect.h-20
		#print(ourShip.rect.w)
		w=ourShip.rect.w
		h=ourShip.rect.h

		ourShip.image = pygame.transform.scale(ourShip.image, (w, h))

	elif event.key == pygame.K_SPACE:
		fire_bullet(my_settings,screen,ourShip,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_RETURN and not stats.game_active:
		restart_game(stats,my_settings,screen,allians,ourShip)

def Keyup(event,ourShip,screen):
	if event.key == pygame.K_RIGHT:
		ourShip.move_right = False		
	elif event.key == pygame.K_LEFT:
		ourShip.move_left = False
	elif event.key == pygame.K_UP:
		ourShip.move_up = False
	elif event.key == pygame.K_DOWN:
		ourShip.move_down = False

def restart_game(stats,my_settings,screen,allians,ourShip):

	stats.game_active=True
	my_settings.ship_limit = 2
	my_settings.Difficulty = 1
	my_settings.Max_allians = 5
	creat_fleet(my_settings,screen,allians,stats)	
	ourShip.center()

def Game_event(ourShip,bullets,screen,my_settings,button1,stats,allians):
	

	pygame.mouse.set_visible(not stats.game_active)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			Keydown(event,ourShip,bullets,screen,my_settings,stats,allians)	
		elif event.type == pygame.KEYUP:
			Keyup(event,ourShip,screen)		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			if  button1.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
				restart_game(stats,my_settings,screen,allians,ourShip)
		
				

def Update_ship(ourShip):
	ourShip.blitme()		
	#bullets.update_bullet()
	ourShip.update_position()

		

def run_game():
	bullets = Group()
	my_settings=Settings()
	stats = GameStats(my_settings)

	pygame.init()
	screen = pygame.display.set_mode(my_settings.screen_para())
	bg_color=my_settings.screen_color
	pygame.display.set_caption("Allian Invasion")

	allians = Group()
	

	button1= Button(my_settings,screen,"Play")
	ourShip = Ship(screen)


	sb1 = Scoreboard(my_settings,screen,stats)	
	sb2 = Scoreboard(my_settings,screen,stats)
 	

	while True:
		screen.fill(bg_color)
		Game_event(ourShip,bullets,screen,my_settings,button1,stats,allians)
		if stats.game_active:
			sb1.prep_score(my_settings.ScoreA_pos,stats.ship_left)
			sb2.prep_score(my_settings.ScoreP_pos,stats.points)
			sb1.show_score()
			sb2.show_score()
			
			Update_ship(ourShip)			
			update_bullets(my_settings,bullets,allians,screen,stats)			
			update_Allians(my_settings,bullets,allians,screen,ourShip,stats)
			
		else:
			button1.draw_button()

		#for allian in allians.sprites():
			#allian.blitme()
			#allian.update()

		pygame.display.flip()
		clock.tick(80)
run_game()