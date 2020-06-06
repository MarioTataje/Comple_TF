import pygame
from pygame.locals import (
    KEYDOWN,
    K_ESCAPE
)


class Standby:
    def __init__(self, width, height):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.tittle = pygame.display.set_caption("Standby")
        self.white = (255, 255, 255)

    def run(self, _running):
        while _running:
            self.screen.fill(self.white)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        _running = False

            pygame.display.update()

        pygame.quit()
        quit()

