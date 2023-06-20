import pygame
from game import Game
from player import Player

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("images/menu.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
<<<<<<< HEAD
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
=======


def new_game(screen, player1, player2):
    game = Game(screen, player1, player2)
    game.run()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player1 = Player("con cac", pygame.image.load("images/x.png"))
            player2 = Player("cai lon", pygame.image.load("images/o.png"))
            new_game(screen, player1, player2)
    screen.blit(background, (0, 0))
    pygame.display.update()
>>>>>>> 2c53054c0144f2929e609f096e83af1a9f360afd
