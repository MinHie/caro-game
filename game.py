import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))

background_color = (168, 96, 93)

tic = pygame.transform.scale(pygame.image.load('images/x.png'), (52, 52))
toe = pygame.transform.scale(pygame.image.load('images/o.png'), (52, 52))
board = pygame.transform.scale(
    pygame.image.load('images/board.png'), (168, 168))

board_x = 10
board_y = 10

running = True
while running:
    screen.fill(background_color)
    screen.blit(board, (10, 10))
    screen.blit(tic, (board_x+1, board_y+1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
