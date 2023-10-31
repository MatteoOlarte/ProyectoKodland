import pygame
from pygame.transform import rotate, scale2x

F14_NORMAL_IMG = pygame.transform.scale2x(pygame.image.load('assets/images/f14_player_1.png'))
F14_ATTACK_IMG = pygame.transform.scale2x(pygame.image.load('assets/images/f14_player_2.png'))

ENEMIES = {
    "f14-normal": scale2x(rotate(pygame.image.load('assets/images/f14_enemy_1.png'), 180)),
    "f14-attack": scale2x(rotate(pygame.image.load('assets/images/f14_enemy_2.png'), 180)),
    "basic_plane": scale2x(rotate(pygame.image.load('assets/images/plane_enemy_1.png'), 180))
}
BULLET = pygame.image.load('assets\images\pixel_gun.png')