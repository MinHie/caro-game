import pygame
import os

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BOARD_SIZE = 336
BOARD_LINE = 6
SQUARE_SIZE = 100
MARGIN = 10
TIC_SIZE = 90

x_win = pygame.transform.scale(pygame.image.load("images/x_won.png"), (250, 50))
o_win = pygame.transform.scale(pygame.image.load("images/o_won.png"), (250, 50))

background_color = (168, 96, 93)


# Vẽ ký hiệu 'X' hoặc 'O' trên màn hình
def draw_xo(x, y, player):
    if player == 1:
        tic = pygame.transform.scale(
            pygame.image.load("images/x.png"), (TIC_SIZE, TIC_SIZE)
        )
    else:
        tic = pygame.transform.scale(
            pygame.image.load("images/o.png"), (TIC_SIZE, TIC_SIZE)
        )
    text_rect = tic.get_rect(center=(x + BOARD_LINE, y + BOARD_LINE))
    screen.blit(tic, text_rect)


# Kiểm tra xem người chơi có thắng hay không
def check_win(board, player):
    # Check rows
    for i in range(len(board)):
        count = 0
        for j in range(len(board[i])):
            if board[i][j] == player:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0

    # Check columns
    for j in range(len(board[0])):
        count = 0
        for i in range(len(board)):
            if board[i][j] == player:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0

    # Check diagonal (top-left to bottom-right)
    for i in range(len(board) - 4):
        for j in range(len(board[i]) - 4):
            count = 0
            for k in range(5):
                if board[i + k][j + k] == player:
                    count += 1
                    if count == 5:
                        return True

    # Check diagonal (top-right to bottom-left)
    for i in range(4, len(board)):
        for j in range(len(board[i]) - 4):
            count = 0
            for k in range(5):
                if board[i - k][j + k] == player:
                    count += 1
                    if count == 5:
                        return True

    return False


# Vẽ lưới
def draw_grid():
    board = pygame.transform.scale(
        pygame.image.load("images/board.png"), (BOARD_SIZE, BOARD_SIZE)
    )
    board_x = 10
    board_y = 10
    x = BOARD_SIZE - BOARD_LINE
    for i in range(0, 3):
        for j in range(0, 2):
            screen.blit(board, (board_x + x * i, board_y + x * j))


# Khởi tạo bảng và người chơi
num_rows = 12
num_cols = 12
board = [[0 for j in range(num_cols)] for i in range(num_rows)]
current_player = 1
player_win = 0

# Vòng lặp chính của trò chơi
running = True
while running:
    # Xử lý sự kiện từ người dùng
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and player_win == 0:
            # Lấy tọa độ của chuột khi người dùng click vào màn hình
            x, y = pygame.mouse.get_pos()
            # Tính toán vị trí của ô vuông tương ứng với tọa độ của chuột
            row = (y - MARGIN) // (SQUARE_SIZE + MARGIN)
            col = (x - MARGIN) // (SQUARE_SIZE + MARGIN)
            # Đặt ký hiệu 'X' hoặc 'O' vào ô vuông tương ứng và chuyển lượt cho người chơi khác
            if board[row][col] == 0:
                board[row][col] = current_player
                if check_win(board, current_player):
                    print(f"Player {current_player} wins!")
                    player_win = current_player
                else:
                    current_player = 2 if current_player == 1 else 1

    # Vẽ lưới và các ký hiệu 'X' hoặc 'O' lên màn hình
    screen.fill(background_color)
    draw_grid()
    for i in range(num_cols):
        for j in range(num_rows):
            if board[i][j] != 0:
                x = 10 * (j + 1) + SQUARE_SIZE * j + SQUARE_SIZE // 2
                y = 10 * (i + 1) + SQUARE_SIZE * i + SQUARE_SIZE // 2
                draw_xo(x, y, board[i][j])

    if player_win != 0:
        if player_win == 1:
            screen.blit(x_win, ((SCREEN_WIDTH - 250) / 2, (SCREEN_HEIGHT - 50) / 2))
        if player_win == 2:
            screen.blit(o_win, ((SCREEN_WIDTH - 250) / 2, (SCREEN_HEIGHT - 50) / 2))
    # Cập nhật màn hình
    pygame.display.update()
# Kết thúc trò chơi và đóng cửa sổ
pygame.quit()
