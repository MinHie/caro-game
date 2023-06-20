import pygame
from game import Game
from player import Player
from button import Button

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("images/menu.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


def new_game(screen, player1, player2):
    game = Game(screen, player1, player2)
    game.run()


while True:
    MENU_MOUSE_POS = pygame.mouse.get_pos()

    screen.blit(background, (0, 0))

    img_play = pygame.image.load("images/play_button.png")
    img_play1 = pygame.image.load("images/play_button_1.png")
    play_button = Button(
        pygame.transform.scale(img_play, (250, 90)),
        pygame.transform.scale(img_play1, (250, 90)),
        pos=(640, 300),
    )

    img_quit = pygame.image.load("images/quit_button.png")
    img_quit1 = pygame.image.load("images/quit_button_1.png")
    quit_button = Button(
        pygame.transform.scale(img_quit, (250, 90)),
        pygame.transform.scale(img_quit1, (250, 90)),
        pos=(640, 400),
    )
    for button in [play_button, quit_button]:
        button.check_hover(MENU_MOUSE_POS)
        button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.check_click(MENU_MOUSE_POS):
                player1 = Player("con cac", pygame.image.load("images/x.png"))
                player2 = Player("cai lon", pygame.image.load("images/o.png"))
                new_game(screen, player1, player2)
            if quit_button.check_click(MENU_MOUSE_POS):
                pygame.quit()

    pygame.display.update()
