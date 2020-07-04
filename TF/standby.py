import pygame
from pygame.locals import (
    KEYDOWN,
    K_ESCAPE
)
from dice import Dice


class Standby:
    def __init__(self, width, height):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.tittle = pygame.display.set_caption("Standby")
        self.image = pygame.image.load("Standby.png")
        self.scaledImage = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
        self.gray = (128, 128, 128)
        self.newGray = (55, 118, 118)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.Verify = False
        self.diceImage = 0
        self.n = 0

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

    def throwDice(self):
        dice = Dice()
        self.n = dice.drawDice()
        self.Verify = True
        self.diceImage = dice.dice

        target = [
            [1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1]
         ]

        sideLength = 40
        row = 0
        column = 0

        for matrixRow in target:
            for element in matrixRow:
                if element != 0:
                    pygame.draw.rect(self.screen, self.red, (column * sideLength, row * sideLength , sideLength, sideLength), 2)
                column = column + 1
            column = 0
            row = row + 1



    def run(self, _running):
        while _running:
            self.screen.blit(self.scaledImage, (0, 0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        _running = False

            self.button(15, 20, 100, 40, 'Throw', self.throwDice)
            if self.Verify:
                self.screen.blit(self.diceImage, (140, 5))
            pygame.display.update()

        pygame.quit()
        quit()

