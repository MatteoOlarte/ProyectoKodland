import pygame
import random
import pygame_widgets
from pygame_widgets.button import Button
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

    def open_menu(self):
        run = True

        while run:
            label = self.waring_font.render("Spacial Wars", True, (0, 0, 0))
            self.display.fill((255, 255, 255))
            self.display.blit(
                label, (self.resolucion[0]/2 - label.get_width()/2, 200))

            # Crear Botones
            easy_btn = Button(
                self.display,
                (self.resolucion[0]/2 - 100),
                300,
                200,
                50,
                text="Modo Facil",
                onClick=lambda:self.start(1))
            
            medium_btn = Button(
                self.display,
                (self.resolucion[0]/2 - 100),
                400,
                200,
                50,
                text="Modo Normal",
                onClick=lambda:self.start(2))
            
            hard_btn = Button(
                self.display,
                (self.resolucion[0]/2 - 100),
                500,
                200,
                50,
                text="Modo Dificil",
                onClick=lambda:self.start(3))
            
            events = pygame.event.get()
            for event in events:
                run = not event.type == pygame.QUIT

            easy_btn.draw()
            medium_btn.draw()
            hard_btn.draw()
            self.clock.tick(60)
            pygame.display.update()
            pygame_widgets.update(events)
        

    def get_player(self):
        match self.difficulty:
            case 1: return Player(0, 0, F14_TOMCAT_N)
            case 2: return Player(0, 0, F14_TOMCAT_S)
            case 3: return Player(0, 0, F18_SH)

    def start(self, difficulty):
        # Crear bucle del juego
        run = True
        game_over_counter = 0
        self.difficulty = difficulty
        self.player = self.get_player()
        self.player.x = (Game.resolucion[0] - self.player.width) / 2
        self.player.y = Game.resolucion[1] - self.player.health - 5
        print(self.player.cooldown)

        while run:
            # el juego corre a un framerate de 15 cuadros por segundo
            self.redraw()
            self.clock.tick(30)

            for event in pygame.event.get():
                run = not event.type == pygame.QUIT

            # logica del el spawn de enemigos
            self.spawn_enemies()
            for enemy in self.enemies[:]:
                if random.randrange(0, 4*30) == 1:
                    enemy.shoot()

                if is_colliding(self.player, enemy):
                    self.enemies.remove(enemy)
                    self.player.health -= 5

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
                game_over_counter += 1

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
        points_label = self.font.render(f"Dificultad: {self.difficulty}", 1, (255, 255, 255))
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
    g.open_menu()
