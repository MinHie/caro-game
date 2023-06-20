import pygame
from board import Board
from player import Player

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (168, 96, 93)
BOARD_SIZE = 336
BOARD_LINE = 6
SQUARE_SIZE = 100
MARGIN = 10
TIC_SIZE = 90
COLUMNS = 9
ROWS = 6

class Game:
    def __init__(self, player1: Player, player2: Player):
        self.board = Board(COLUMNS, ROWS)
        self.players = [player1, player2]
        self.current_player = 0
        self.player_win = False

    def check_win(self):
        # Check rows
        for i in range(len(self.board.matrix)):
            count = 0
            for j in range(len(self.board.matrix[i])):
                if self.board.matrix[i][j] == self.current_player:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0

        # Check columns
        for j in range(len(self.board.matrix[0])):
            count = 0
            for i in range(len(self.board.matrix)):
                if self.board.matrix[i][j] == self.current_player:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0

        # Check diagonal (top-left to bottom-right)
        for i in range(len(self.board.matrix) - 4):
            for j in range(len(self.board.matrix[i]) - 4):
                count = 0
                for k in range(5):
                    if self.board.matrix[i + k][j + k] == self.current_player:
                        count += 1
                        if count == 5:
                            return True

        # Check diagonal (top-right to bottom-left)
        for i in range(4, len(self.board.matrix)):
            for j in range(len(self.board.matrix[i]) - 4):
                count = 0
                for k in range(5):
                    if self.board.matrix[i - k][j + k] == self.current_player:
                        count += 1
                        if count == 5:
                            return True

        return False

    def draw_xo(self, x, y, player: Player):
        tic = pygame.transform.scale(player.symbol, (TIC_SIZE, TIC_SIZE))
        text_rect = tic.get_rect(center=(x + BOARD_LINE, y + BOARD_LINE))
        self.screen.blit(tic, text_rect)

    def draw(self):
        self.board.draw(self.screen, BOARD_SIZE, BOARD_LINE)

        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.board.matrix[i][j] != -1:
                    x = 10 * (j + 1) + SQUARE_SIZE * j + SQUARE_SIZE // 2
                    y = 10 * (i + 1) + SQUARE_SIZE * i + SQUARE_SIZE // 2
                    player = self.players[self.board.matrix[i][j]]
                    self.draw_xo(x, y, player)
        
        if self.player_win:
            if self.current_player == 0:
                x_win = pygame.transform.scale(pygame.image.load("images/x_won.png"), (250, 50))
                self.screen.blit(x_win, ((SCREEN_WIDTH - 250) / 2, (SCREEN_HEIGHT - 50) / 2))
            if self.current_player == 1:
                o_win = pygame.transform.scale(pygame.image.load("images/o_won.png"), (250, 50))
                self.screen.blit(o_win, ((SCREEN_WIDTH - 250) / 2, (SCREEN_HEIGHT - 50) / 2))
                    
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Caro Game")
        player_win = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and not self.player_win:
                    x, y = pygame.mouse.get_pos()

                    row = (y - MARGIN) // (SQUARE_SIZE + MARGIN)
                    col = (x - MARGIN) // (SQUARE_SIZE + MARGIN)

                    player = self.players[self.current_player]
                    self.board.mark(row, col, self.current_player)

                    for i in self.board.matrix:
                        print(i)

                    if self.check_win():
                        print("Player " + player.name + " win")
                        self.player_win = True

                    print("//")
                    print(self.current_player)

                    self.current_player = (self.current_player + 1) % 2 if not self.player_win else self.current_player

            self.screen.fill(BACKGROUND_COLOR)

            self.draw()
            
            pygame.display.update()
