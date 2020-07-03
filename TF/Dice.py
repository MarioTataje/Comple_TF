import pygame
from pygame.locals import (
    KEYDOWN,
    K_ESCAPE
)
from random import randint


class Dice:

    def __init__(self):
        self.x = 550
        self.y = 400
        self.dice = 0

    def drawdice(self):
        n = randint(1, 6)
        if n == 1:
            self.dice = pygame.image.load('imagen1')
            self.dice = pygame.transform.scale(self.dice, (100, 100))
        elif n == 2:
            self.dice = pygame.image.load('imagen2')
            self.dice = pygame.transform.scale(self.dice, (100, 100))
        elif n == 3:
            self.dice = pygame.image.load('imagen3')
            self.dice = pygame.transform.scale(self.dice, (100, 100))
        elif n == 4:
            self.dice = pygame.image.load('imagen4')
            self.dice = pygame.transform.scale(self.dice, (100, 100))
        elif n == 5:
            self.dice = pygame.image.load('imagen5')
            self.dice = pygame.transform.scale(self.dice, (100, 100))
        elif n == 6:
            self.dice = pygame.image.load('imagen6')
            self.dice = pygame.transform.scale(self.dice, (100, 100))
        return n

#def lanzar_dado():
#    return randint(1, 6)
#dado = lanzar_dado()

#print(f"El dado ha caido en : {dado}")

