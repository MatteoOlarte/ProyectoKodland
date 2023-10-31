import pygame
import elementos
from mundo import *


class Game:
    resolucion = (640, 680)
    waring_font = None

    def __init__(self, difficulty=1) -> None:
        pygame.init()
        pygame.display.set_caption("Spacial Wars")
        self.display = pygame.display.set_mode(Game.resolucion)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Consolas", 20)
        self.player = None
        self.difficulty = difficulty
        self.enemies = []
        self.lives = 10 - difficulty 
        self.points = 0
        self.lost = False
        Game.waring_font = pygame.font.SysFont("Consolas", 50, True)

    def start(self):
        # Crear bucle del juego
        run = True
        game_over_counter = 0
        self.player = Player(0, 0, F14_TOMCAT_N)
        self.player.x = (Game.resolucion[0] - self.player.width) / 2
        self.player.y = Game.resolucion[1] - self.player.health - 5

        while run:
            # el juego corre a un framerate de 15 cuadros por segundo
            self.redraw()
            self.clock.tick(30)

            for event in pygame.event.get():
                run = not event.type == pygame.QUIT

            # logica del el spawn de enemigos
            self.spawn_enemies()
            for enemy in self.enemies[:]:
                if enemy.y > Game.resolucion[1]:
                    self.enemies.remove(enemy) 
                    self.lives -= 1
                else:
                    enemy.move()
                    enemy.update_shoots(enemy.seed, self.player)

            self.player.update_shoots(-self.player.seed, self.enemies)
            # logica de perder el juego
            if self.lives <= 0 or self.player.health <= 0:  
                self.lost = True
                game_over_counter+=1

            if self.lost:
                if game_over_counter > 150:
                    run = False
                else:
                    continue

            # registrar las teclas presionadas por el usuario
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.player.x + 5 > 0:
                self.player.x -= self.player.seed
            if keys[pygame.K_d] and self.player.x + 5 < Game.resolucion[0]:
                self.player.x += self.player.seed
            if keys[pygame.K_SPACE]:
                self.player.shoot()

    def redraw(self):
        # dibujar pantalla
        self.display.fill((0, 0, 0))

        # textos de informacion
        points_label = self.font.render(f"Puntos: 3", 1, (255, 255, 255))
        lives_label = self.font.render(
            f"Vidas: {self.lives}", 1, (255, 255, 255))

        # dibujar jugador
        self.display.blit(
            points_label, (10, Game.resolucion[1] - points_label.get_height() - 10))
        self.display.blit(
            lives_label, (10, Game.resolucion[1] - points_label.get_height() - lives_label.get_height() - 10))
        self.player.draw(self.display)

        # dibujar enemigos
        for enemy in self.enemies:
            enemy.draw(self.display)

        # pantalla "GAME OVER"
        if self.lost:
            label = Game.waring_font.render("GAME OVER", 1, (255, 0, 0))
            self.display.blit(
                label, (Game.resolucion[0]/2 - label.get_width()/2, 300))

        pygame.display.update()

    def spawn_enemies(self):

        if len(self.enemies) == 0:
            for _ in range(self.difficulty * 3):
                e = Enemy(
                    random.randint(0, Game.resolucion[0] - 100),
                    random.randint(-1000, -100),
                    random.choice(ENEMY_AIRCRAFT)
                )
                self.enemies.append(e)


if __name__ == '__main__':
    g = Game()
    g.start()
