import pygame
from manejador import Manejador
pygame.init()

running = True

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Ubongo")
image = pygame.image.load("ubongo.png")

while running:

    screen.blit(image, (0, 0))
    pygame.display.update()

pygame.quit()
quit()

