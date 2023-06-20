import pygame
from game import Game
from player import Player

if __name__ == "__main__":  
    player1 = Player("con cac", pygame.image.load("images/x.png"))
    player2 = Player("cai lon", pygame.image.load("images/o.png"))
    game = Game(player1, player2)
    game.run()