import pygame
from pygame.sprite import Sprite
from random import randint
class Settings():
	def __init__(self):
		self.sreen_width=1600
		self.screen_hight=1200
		self.screen_color=(230,230,230)

		self.speed_ship_factor = 5
		self.ship_limit = 2
		#Bullet Settings
		self.bullet_speed_factor = 10
		self.df = 5
		self.bullet_height = 30
		self.bullet_color = 60,60,60
		self.bullets_allow = 5
		self.Difficulty = 1
		self.Max_allians = 5

		self.ScoreA_pos = "left"
		self.ScoreP_pos = "right"
	def screen_para(self):
		return ( self.sreen_width,self.screen_hight)

class Ship:

	def __init__(self,screen):

		self.all_settings = Settings()
		self.screen=screen

		self.image=pygame.image.load('ship.png')
		#to slace big ship
		self.image=pygame.transform.scale(self.image, (100, 160))
		self.screen_rect = screen.get_rect()

		self.rect = self.image.get_rect()
		# To place the player at the midleft.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		#self.rect.midleft = self.screen_rect.midleft

		#Moving flags
		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False 

	def update_position(self):
		if self.move_right:			
				self.rect.centerx +=self.all_settings.speed_ship_factor
		if self.move_left:	
				self.rect.centerx -=self.all_settings.speed_ship_factor
		if self.move_up:	
				self.rect.centery -=self.all_settings.speed_ship_factor
		if self.move_down:	
				self.rect.centery +=self.all_settings.speed_ship_factor

	def blitme(self):

		self.screen.blit(self.image,self.rect)

	def center(self):
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
class Allian(Sprite):

	def __init__(self,ai_settings,screen):
		super(Allian,self).__init__()
		self.screen = screen
		self.Settings = ai_settings

		self.Difficulty = self.Settings.Difficulty

		self.speed = randint(self.Difficulty,2*self.Difficulty)
		self.direction = 1
		self.drop_speed = 5


		self.image = pygame.image.load('Allian.png')
		self.image=pygame.transform.scale(self.image, (100, 160))
		self.rect = self.image.get_rect()

		print(self.rect.width,self.rect.height)
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def blitme(self):
			self.screen.blit(self.image,self.rect)

	def move_foward(self):
		#print(abs(self.speed))
		self.rect.y+=self.Difficulty*100

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			#self.direction*=-1
			#self.move_foward()
			return True
		elif self.rect.left <=0:
			#self.direction*=-1
			#self.move_foward()
			return True
		else:
			return False

	def check_bottom(self):
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom:
			return True	
		else:
			return False

	def update(self):
		if self.speed==0:
			self.speed=-7
		#if (self.check_edges()

		self.rect.x+=self.speed*self.direction
