import pygame
from game import Game
from player import Player

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("images/menu.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pass

#     screen.blit(background, (0, 0))
#     pygame.display.update()

pygame.init()
player1 = Player("con cac", pygame.image.load("images/x.png"))
player2 = Player("cai lon", pygame.image.load("images/o.png"))
game = Game(screen, player1, player2)
game.run()
