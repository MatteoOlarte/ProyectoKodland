import elementos
import pygame
from pygame import Surface


class Plane:
    def __init__(self, x, y, image: Surface, health, damage, speed, cooldown = 30) -> None:
        self.max_cooldown = cooldown
        self.x = x
        self.y = y
        self.shoots = []
        self.image: Surface = image
        self.gun_image = elementos.BULLET
        self.seed = speed
        self.health = health
        self.damage = damage
        self.MAX_HEALTH = health
        self.height = image.get_height()
        self.width = image.get_width()
        self.dt_count = 0


    def draw(self, surface: Surface):
        surface.blit(self.image, (self.x, self.y))

        for s in self.shoots:
            s.draw(surface)

    def cooldown(self):
        if self.dt_count >= self.max_cooldown:
            self.dt_count = 0
        elif self.dt_count > 0:
            self.dt_count += 1

    def shoot(self):
        if self.dt_count == 0:
            shoot = Bullet(self.x, self.y)
            self.shoots.append(shoot)
            self.dt_count = 1


    def update_shoots(self, velocity, surface):
        self.cooldown()
        for bullet in self.shoots:
            bullet.move(velocity + 10)

            if bullet.y < 0 or bullet.y > 999:
                self.shoots.remove(bullet)
            elif bullet.colision(surface) and type(surface) is Player:
                print(type(surface))
                surface.health -= self.damage
                print(surface.health)
                self.shoots.remove(bullet)


class Player(Plane):

    def __init__(self, x, y, plane: Plane) -> None:
        Plane.__init__(self, x, y,
                       plane.image,
                       plane.health,
                       plane.damage,
                       plane.seed,
                       plane.max_cooldown)
        self.mask = pygame.mask.from_surface(plane.image)

    def update_shoots(self, velocity, enemies):
        self.cooldown()
        for bullet in self.shoots:
            bullet.move(velocity)

            if bullet.y < 0 or bullet.y > 999:
                self.shoots.remove(bullet)
            else:
                for enemy in enemies:
                    if bullet.colision(enemy):
                        enemies.remove(enemy)
                        self.shoots.remove(bullet)

    def draw(self, surface: Surface):
        super().draw(surface)
        self.draw_heath_bar(surface)

    def draw_heath_bar(self, surface: Surface):
        max_height = 5
        max_width = self.width
        position_x = self.x
        position_y = self.y + self.height + 10
        completed = (self.health * max_width) / self.MAX_HEALTH

        # barra interna
        pygame.draw.rect(surface, (255, 0, 0), (position_x,
                         position_y, max_width, max_height))

        # barra externa
        pygame.draw.rect(surface, (0, 255, 0), (position_x,
                         position_y, completed, max_height))


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


class Bullet:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.image = elementos.BULLET
        self.mask = pygame.mask.from_surface(self.image)
        pass

    def draw(self, window: Surface):
        window.blit(self.image, (self.x, self.y))

    def colision(self, obj):
        return is_colliding(obj, self)

    def move(self, speed):
        self.y += speed


def is_colliding(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


F14_TOMCAT_N = Plane(0, 0, elementos.F14_NORMAL_IMG, 120, 30, 4)
F14_TOMCAT_S = Plane(0, 0, elementos.F14_ATTACK_IMG, 120, 30, 4.5, cooldown=25)
F18_SH = Plane(0, 0, elementos.F14_ATTACK_IMG, 200, 35, 5.5, cooldown=15)

ENEMY_AIRCRAFT = (
    Plane(0, 0, elementos.ENEMIES['f14-normal'], 120, 30, 4),
    Plane(0, 0, elementos.ENEMIES['f14-attack'],
          120, 30, 4.2),  # 5% mas rapido
    Plane(0, 0, elementos.ENEMIES['basic_plane'], 90, 10, 2.5)
)
