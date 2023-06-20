import pygame
from game import Game
from player import Player

player1 = Player(1, pygame.image.load("images/x.png"))
player2 = Player(2, pygame.image.load("images/o.png"))
game = Game(player1, player2)
game.run()
