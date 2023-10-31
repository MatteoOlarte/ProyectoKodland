import elementos
import pygame
import random
from pygame import Surface


class Plane:
    def __init__(self, x, y, image: Surface, health, damage, speed) -> None:
        self.x = x
        self.y = y
        self.guns = []
        self.image: Surface = image
        self.gun_image = elementos.BULLET
        self.seed = speed
        self.health = health
        self.damage = damage
        self.MAX_HEALTH = health
        self.height = image.get_height()
        self.width = image.get_width()

    def draw(self, surface: Surface):
        surface.blit(self.image, (self.x, self.y))


class Player(Plane):
    def __init__(self, x, y, plane: Plane) -> None:
        Plane.__init__(self, x, y, 
                       plane.image, 
                       plane.health,
                       plane.damage, 
                       plane.seed)
        self.mask = pygame.mask.from_surface(plane.image)

    def draw(self, surface: Surface):
        surface.blit(self.image, (self.x, self.y))


class Enemy(Plane):
    def __init__(self, x, y, plane: Plane) -> None:
        Plane.__init__(self, 
                       x, 
                       y, 
                       plane.image,
                       plane.health,
                       plane.damage, 
                       plane.seed)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.y += self.seed


F14_TOMCAT_N = Plane(0, 0, elementos.F14_NORMAL_IMG, 120, 30, 4)
F14_TOMCAT_S = Plane(0, 0, elementos.F14_ATTACK_IMG, 120, 30, 4.5)
F18_SH = Plane(0, 0, elementos.F14_ATTACK_IMG, 200, 35, 5)

ENEMY_AIRCRAFT = (
    Plane(0, 0, elementos.ENEMIES['f14-normal'], 120, 30, 4),
    Plane(0, 0, elementos.ENEMIES['f14-attack'], 120, 30, 4.2), # 5% mas rapido
    Plane(0, 0, elementos.ENEMIES['basic_plane'], 90, 10, 2.5)
)