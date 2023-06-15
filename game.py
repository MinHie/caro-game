import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))

image_path = "caro-game/images/background.png"
original_image = pygame.image.load(image_path)
scaled_image = pygame.transform.scale(original_image, (80, 60))


screen.blit(scaled_image, (0, 0))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()