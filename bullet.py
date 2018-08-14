import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

	def __init__(self,Settings,screen,ship):


		#creat bullet object right at spaceship
		super(Bullet,self).__init__()
		self.screen = screen

		self.rect = pygame.Rect(0,0,Settings.width,Settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		self.y = float(self.rect.y)

		self.color = Settings.bullet_color
		self.speed_factor = Settings.bullet_speed_factor

	def update_bullet(self):
		self.y -= self.speed_factor
		self.rect.y=self.y
		

	def creat_bullet(self):
		
		pygame.draw.rect(self.screen, self.color, self.rect)