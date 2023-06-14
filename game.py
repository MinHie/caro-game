import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))

background_color = (168, 96, 93)

tic = pygame.transform.scale(pygame.image.load('images/x.png'), (50, 50))
toe = pygame.transform.scale(pygame.image.load('images/o.png'), (50, 50))

running = True
while running:
    screen.fill(background_color)
    screen.blit(tic, (10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
