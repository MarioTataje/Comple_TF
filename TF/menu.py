import pygame
from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
)
from standby import Standby
from instructions import Instructions
import utils

def exitGame():
    pygame.quit()
    quit()


def startGame():
    screen_dimensions = utils.get_screen_dimensions()
    matrix = [
                [0, 0, 1, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 1]
            ]

    pieces = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 1, 9: 0, 10: 0, 11: 0, 12: 0, 13: 1, 14: 0,
                            15: 0, 16: 0, 17: 0, 18: 1, 19: 0}
    standby = Standby(screen_dimensions['width'], screen_dimensions['height'], matrix, pieces)
    standby.run(True)


def instructionsGame():
    screen_dimensions = utils.get_screen_dimensions()
    instructions = Instructions(screen_dimensions['width'], screen_dimensions['height'])
    instructions.run(True)


class Test:
    def __init__(self, width, height):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.tittle = pygame.display.set_caption("Ubongo")
        self.image = pygame.image.load("ubongo.png")
        self.scaledImage = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
        self.gray = (128, 128, 128)
        self.newGray = (55, 118, 118)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.white)
        return textSurface, textSurface.get_rect()

    def button(self, x, y, width, height, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, self.black, ((x - 10) - 2, (y - 10) - 2, (width + 20) + 4, (height + 20) + 4), 0)
            pygame.draw.rect(self.screen, self.newGray, (x - 10, y - 10, width + 20, height + 20))
            word = pygame.font.SysFont('comicsans', 30)

            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(self.screen, self.black, (x - 2, y - 2, width + 4, height + 4), 0)
            pygame.draw.rect(self.screen, self.gray, (x, y, width, height))
            word = pygame.font.SysFont('comicsans', 25)

        textSurf, textRect = self.text_objects(text, word)
        textRect.center = ((x + int((width / 2))), (y + int((height / 2))))
        self.screen.blit(textSurf, textRect)

    def run(self, _running):
        while _running:
            self.screen.blit(self.scaledImage, (0, 0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        _running = False

            self.button((self.screen_width/2) - 65, (self.screen_height/2) + 120, 130, 40, 'Play', startGame)
            self.button((self.screen_width/2) - 65, (self.screen_height/2) + 180, 130, 40, 'Instructions', instructionsGame)
            self.button((self.screen_width/2) - 65, (self.screen_height/2) + 240, 130, 40, 'Exit', exitGame)
            pygame.display.update()

        pygame.quit()
        quit()

screen_dimensions = utils.get_screen_dimensions()

test = Test(screen_dimensions['width'], screen_dimensions['height'])
test.run(True)
