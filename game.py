import pygame
from board import Board
from player import Player

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
SIZE = 2
BOARD_SIZE = 58 * SIZE
BOARD_LINE = 1 * SIZE
SQUARE_SIZE = 20 * SIZE
TIC_SIZE = 16 * SIZE
COLUMNS = 32
ROWS = 18
BACKGROUND_COLOR = (168, 96, 93)


class Game:
    def __init__(self, screen, player1: Player, player2: Player):
        self.screen = screen
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
        self.screen.blit(tic, (x, y))

    def draw(self):
        self.board.draw(
            self.screen, BOARD_SIZE, BOARD_LINE, int(ROWS / 3), int(COLUMNS / 3)
        )

        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.board.matrix[i][j] != -1:
                    x = 10 + BOARD_LINE * 2 + (SQUARE_SIZE - BOARD_LINE) * j
                    y = 10 + BOARD_LINE * 2 + (SQUARE_SIZE - BOARD_LINE) * i
                    player = self.players[self.board.matrix[i][j]]
                    self.draw_xo(x, y, player)

        if self.player_win:
            rect = ((SCREEN_WIDTH - 500) / 2, (SCREEN_HEIGHT - 100) / 2)
            if self.current_player == 0:
                img = pygame.image.load("images/x_won.png")
            else:
                img = pygame.image.load("images/o_won.png")
            win = pygame.transform.scale(img, (500, 100))
            self.screen.blit(win, rect)

    def run(self):
        pygame.display.set_caption("Caro Game")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and not self.player_win:
                    x, y = pygame.mouse.get_pos()

                    col = (x - BOARD_LINE * 2) // (SQUARE_SIZE - BOARD_LINE)
                    row = (y - BOARD_LINE * 2) // (SQUARE_SIZE - BOARD_LINE)

                    if self.board.matrix[row][col] == -1:
                        player = self.players[self.current_player]
                        self.board.mark(row, col, self.current_player)

                        if self.check_win():
                            print("Player " + player.name + " win")
                            self.player_win = True

                        self.current_player = (
                            (self.current_player + 1) % 2
                            if not self.player_win
                            else self.current_player
                        )

            self.screen.fill(BACKGROUND_COLOR)

            self.draw()

            pygame.display.update()
