import pygame


class Board:
    def __init__(self, num_cols, num_rows):
        self.matrix = [[0 for j in range(num_cols)] for i in range(num_rows)]

    def draw(self, screen, BOARD_SIZE, BOARD_LINE):
        img = pygame.image.load("images/board.png")
        board = pygame.transform.scale(img, (BOARD_SIZE, BOARD_SIZE))
        board_x = 10
        board_y = 10
        x = BOARD_SIZE - BOARD_LINE
        for i in range(0, 3):
            for j in range(0, 2):
                screen.blit(board, (board_x + x * i, board_y + x * j))

    def mark(self, row, col, player):
        if self.matrix[row][col] == 0:
            self.matrix[row][col] = player
            