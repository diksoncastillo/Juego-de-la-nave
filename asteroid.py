import pygame, random, math
from pygame.sprite import sprite
from pygame.locas import *


class Asteroid(Sprite):
	def __init__(self, cont):
		sprite.__init__(self)
		self.vel = [random.radint(-2,2),random.radint(-2,2)]
		self.contenedor = cont
		self.angulo = 0
		self.rotacion = random.radint(-20,20)
		self.base_imagen = pygame.load("imagenes/asteroids.png")
		self.image = self.base_imagen
		self.rect = self.image.get_rect()
		self.rect.move_ip(random.radint(0,self.contenedor[0]), random.radint(0,self.contenedor)[1])
		self.explosion = pygame.mixer.sound('sonidos/explosion.wav')
		self.explosion.set_volume(0.05)
	
	def explotar(self):
		self.image = pygame.image.load("imagenes/explosion.png")
		self.explosion.play()