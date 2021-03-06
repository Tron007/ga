
import pygame.font
from Settings import Ship_lvlimage
from pygame.sprite import Group
class GameStats():

	 def __init__(self,ai_settings):
	 	self.ai_settings = ai_settings
	 	self.reset_stats()
	 	self.game_active = False

	 	self.ship_left = 0 
	 	self.points = 0 
	 	self.hight_score = 0
	 def reset_stats(self):
	 	self.ship_left = self.ai_settings.ship_limit




class Button():

	def __init__(self,Settings,screen,msg):
		self.screen = screen
		self.screen_rect = screen.get_rect()


		self.width,self.height = 200,50
		self.button_color = (0,255,0)
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None,48)

		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.center = self.screen_rect.center

		self.prep_msg(msg)

	def prep_msg(self,msg):
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	
	def draw_button(self):
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

class Scoreboard():
	def __init__(self,ai_settings,screen,stats):

	 	self.screen =screen
	 	self.screen_rect = screen.get_rect()
	 	self.ai_settings = ai_settings
	 	self.stats = stats


	 	self.text_color = (30,30,30)
	 	self.font = pygame.font.SysFont(None,48)

	 	#prep_score(ai_settings.ScoreA_pos,self.stats.ship_left)
	 	#prep_score(ai_settings.ScoreP_pos,self.stats.points)


	def prep_score(self,position,value,qwe=0):
	 	
	 	
	 	if qwe==0:
	 		rounded_score = int(round(value,-1))
	 		score_str = "{:,}".format(rounded_score)
	 	else:
	 		score_str=str(value)



	 	self.score_image = self.font.render(score_str,True,
	 		self.text_color,self.ai_settings.screen_color)

	 	self.score_rect = self.score_image.get_rect()


	 	if position=="right":
	 		self.score_rect.right=self.screen_rect.right -20
	 	elif position=="left":
	 		self.score_rect.left=self.screen_rect.left +20
	 	else:
	 		self.score_rect.centerx =self.screen_rect.centerx

	 	self.score_rect.top = 20

	def prep_level(self,curlvl):
		score_str="Curent lvl: "+str(curlvl)
		self.lvlImage = self.font.render(score_str,True,
	 		self.text_color,self.ai_settings.screen_color)

		self.lvlImage_rect = self.lvlImage.get_rect()
		self.lvlImage_rect.right=self.screen_rect.right-20
		self.lvlImage_rect.top = self.score_rect.bottom + 10

	def prep_lifes(self):
		self.ships= Group()
		for ship_numer in range(self.ai_settings.ship_limit):
			ship = Ship_lvlimage()
			ship.rect.x = 10 + ship_numer *ship.rect.width
			ship.rect.y = self.screen_rect.y+ship.rect.height+10
			self.ships.add(ship) 

	def show_score(self):
	 	self.screen.blit(self.score_image,self.score_rect)

	def show_lvl(self):
	 	self.screen.blit(self.lvlImage,self.lvlImage_rect)

	def show_life(self):
	 	for ship in self.ships:
	 		self.screen.blit(ship.image,ship.rect)

