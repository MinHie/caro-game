import pygame
from board import Board
from player import Player

x_win = pygame.transform.scale(pygame.image.load("images/x_won.png"), (250, 50))
o_win = pygame.transform.scale(pygame.image.load("images/o_won.png"), (250, 50))
BACKGROUND_COLOR = (168, 96, 93)
BOARD_SIZE = 336
BOARD_LINE = 6
SQUARE_SIZE = 100
MARGIN = 10
TIC_SIZE = 90


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.board = Board(9, 6)
        self.players = [player1, player2]
        self.current_player = player1.number

    def check_win(self, player: Player):
        # Check rows
        for i in range(len(self.board.matrix)):
            count = 0
            for j in range(len(self.board.matrix[i])):
                if self.board.matrix[i][j] == player.number:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0

        # Check columns
        for j in range(len(self.board.matrix[0])):
            count = 0
            for i in range(len(self.board.matrix)):
                if self.board.matrix[i][j] == player.number:
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
                    if self.board.matrix[i + k][j + k] == player.number:
                        count += 1
                        if count == 5:
                            return True

        # Check diagonal (top-right to bottom-left)
        for i in range(4, len(self.board.matrix)):
            for j in range(len(self.board.matrix[i]) - 4):
                count = 0
                for k in range(5):
                    if self.board.matrix[i - k][j + k] == player.number:
                        count += 1
                        if count == 5:
                            return True

        return False

    def draw_xo(self, x, y, player: Player):
        tic = pygame.transform.scale(player.symbol, (TIC_SIZE, TIC_SIZE))
        text_rect = tic.get_rect(center=(x + BOARD_LINE, y + BOARD_LINE))
        self.screen.blit(tic, text_rect)

    def run(self):
        pygame.init()
        SCREEN_WIDTH = 1200
        SCREEN_HEIGHT = 720
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Caro Game")
        player_win = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and player_win == 0:
                    x, y = pygame.mouse.get_pos()

                    row = (y - MARGIN) // (SQUARE_SIZE + MARGIN)
                    col = (x - MARGIN) // (SQUARE_SIZE + MARGIN)

                    player = self.players[self.current_player]
                    self.board.mark(row, col, player.number)
                    if self.check_win(player):
                        print(f"Player {player} wins!")
                        player_win = player
                    else:
                        player = 2 if player == 1 else 1
                    for i in self.board.matrix:
                        print(i)
                    print("//")
                    
                    self.current_player = (self.current_player + 1) % 2

            self.screen.fill(BACKGROUND_COLOR)

            self.board.draw(self.screen, BOARD_SIZE, BOARD_LINE)

            for i in range(6):
                for j in range(9):
                    if self.board.matrix[i][j] != 0:
                        x = 10 * (j + 1) + SQUARE_SIZE * j + SQUARE_SIZE // 2
                        y = 10 * (i + 1) + SQUARE_SIZE * i + SQUARE_SIZE // 2
                        player = self.players[0] if self.board.matrix[i][j] == 1 else self.players[1]
                        self.draw_xo(x, y, player)
            if player_win != 0:
                if player_win == 1:
                    self.screen.blit(x_win, ((SCREEN_WIDTH-250) / 2, (SCREEN_HEIGHT-50) / 2))
                if player_win == 2:
                    self.screen.blit(o_win, ((SCREEN_WIDTH-250) / 2, (SCREEN_HEIGHT-50) / 2))            
            pygame.display.update()
