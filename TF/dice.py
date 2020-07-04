import pygame
from pygame.locals import (
    KEYDOWN,
    K_ESCAPE
)
from random import randint


class Dice:
    def __init__(self):
        self.width = 70
        self.height = 70
        self.dice = 0
        self.n = 0

    def drawDice(self):
        self.n = randint(1, 6)
        if self.n == 1:
            self.dice = pygame.image.load('assets/DiceOne.png')
            self.dice = pygame.transform.scale(self.dice, (self.width, self.height))
        elif self.n == 2:
            self.dice = pygame.image.load('assets/DiceTwo.png')
            self.dice = pygame.transform.scale(self.dice, (self.width, self.height))
        elif self.n == 3:
            self.dice = pygame.image.load('assets/DiceThree.png')
            self.dice = pygame.transform.scale(self.dice, (self.width, self.height))
        elif self.n == 4:
            self.dice = pygame.image.load('assets/DiceFour.png')
            self.dice = pygame.transform.scale(self.dice, (self.width, self.height))
        elif self.n == 5:
            self.dice = pygame.image.load('assets/DiceFive.png')
            self.dice = pygame.transform.scale(self.dice, (self.width, self.height))
        elif self.n == 6:
            self.dice = pygame.image.load('assets/DiceSix.png')
            self.dice = pygame.transform.scale(self.dice, (self.width, self.height))
        return self.n

#def lanzar_dado():
#    return randint(1, 6)
#dado = lanzar_dado()

#print(f"El dado ha caido en : {dado}")

