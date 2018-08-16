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

class Rocket(Sprite):

	def __init__(self,Settings,screen,ship):

		self.cur_time = 0
		self.ani_time = 0.1
		super(Rocket,self).__init__()
		self.screen = screen
		self.all_settings = Settings
		self.bullet_image_arr = []
		self.bullet_image=pygame.image.load('Rocket2.png')
		self.bullet_image=pygame.transform.scale(self.bullet_image, (50, 80))
		self.bullet_image_arr.append(self.bullet_image)

		self.bullet_image=pygame.image.load('Rocket1.png')
		self.bullet_image=pygame.transform.scale(self.bullet_image, (50, 80))
		self.bullet_image_arr.append(self.bullet_image)


		self.rect = self.bullet_image.get_rect()
		self.rect.centerx = ship.rect.centerx

		self.index = 0

		self.rect.top = ship.rect.top
		self.speed_factor =  self.all_settings.bullet_speed_factor

	def update_rocket(self,dt):
		#self.y -= self.speed_factor
		self.cur_time += float(float(dt)/1000)
		#print(self.cur_time)
		if self.cur_time>self.ani_time:
			print("anime")
			self.cur_time=0
			print(self.index)			
			if self.index ==1:
				self.index = 0
			elif self.index ==0:
				self.index = 1
			self.bullet_image = self.bullet_image_arr[self.index]

		self.rect.y-=self.speed_factor

	def creat_rocket(self):
		self.screen.blit(self.bullet_image,self.rect)

class creat_destr(Sprite):
	def __init__(self,screen,rocket):
		super(creat_destr,self).__init__()
		self.rect = pygame.Rect(0,0,rocket.rect.width+500,rocket.rect.height+500)
		self.rect.center = rocket.rect.center
		self.color = 60,60,0
		#pygame.draw.rect(screen, self.color, self.rect)
		pygame.draw.circle(screen, self.color, rocket.rect.center,rocket.rect.width+500) 