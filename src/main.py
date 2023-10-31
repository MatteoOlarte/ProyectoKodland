import pygame
import elementos


class Game:
    resolucion = (640, 480)
    font = pygame.font.SysFont("Consolas", 14)

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Spacial Wars")
        self.display = pygame.display.set_mode(Game.resolucion)
        self.clock = pygame.time.Clock()

    def start(self):
        # Crear bucle del juego
        run = True

        while run:
            for event in pygame.event.get():
                run = not event.type == pygame.QUIT

            # el juego corre a un framerate de 15 cuadros por segundo
            self.redraw()
            self.clock.tick(15)

    def redraw(self):
        pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.start()
