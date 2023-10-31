import pygame
import elementos
from mundo import *


class Game:
    resolucion = (640, 480)

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Spacial Wars")
        self.display = pygame.display.set_mode(Game.resolucion)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Consolas", 20)
        self.player = None

    def start(self):
        # Crear bucle del juego
        run = True
        self.player = Player(0, 0, F14_TOMCAT_N)
        self.player.x = (Game.resolucion[0] - self.player.width) / 2
        self.player.y = Game.resolucion[1] - self.player.health - 5
        
        while run:
            for event in pygame.event.get():
                run = not event.type == pygame.QUIT

            # registrar las teclas presionadas por el usuario
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.player.x + 5 > 0:
                self.player.x -= 3
            if keys[pygame.K_d] and self.player.x + 5 < Game.resolucion[0]:
                self.player.x += 3

            # el juego corre a un framerate de 15 cuadros por segundo
            self.redraw()
            self.clock.tick(30)

    def redraw(self):
        self.display.fill((0, 0, 0))
        points_label = self.font.render(f"Puntos: 3", 1, (255, 255, 255))
        lives_label = self.font.render(f"Vidas: 3", 1, (255, 255, 255))
        self.display.blit(
            points_label, (10, Game.resolucion[1] - points_label.get_height() - 10))
        self.display.blit(
            lives_label, (10, Game.resolucion[1] - points_label.get_height() - lives_label.get_height() - 10))
        self.player.draw(self.display)
        pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.start()
