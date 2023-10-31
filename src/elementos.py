import pygame

F14_NORMAL_IMG = pygame.transform.scale2x(pygame.image.load('assets/images/f14_player_1.png'))
F14_ATTACK_IMG = pygame.transform.scale2x(pygame.image.load('assets/images/f14_player_2.png'))

ENEMIES = {
    "f14": pygame.image.load('assets/images/f14_enemy_1.png'),
    "f14-attack": pygame.image.load('assets/images/f14_enemy_2.png'),
    "basic-enemy": pygame.image.load('assets/images/plane_enemy_1.png')
}

BULLET = pygame.image.load('assets\images\pixel_gun.png')