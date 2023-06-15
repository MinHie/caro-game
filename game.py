import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1200, 720))
SQUARE_SIZE = 100
MARGIN = 0
GRID_SIZE = SQUARE_SIZE * 3 + MARGIN * 4
TIC_SIZE = 94

background_color = (168, 96, 93)
# Vẽ ký hiệu 'X' hoặc 'O' trên màn hình
def draw_xo(x, y, player):
    if player == 1:
        tic = pygame.transform.scale(pygame.image.load('images/x.png'), (TIC_SIZE, TIC_SIZE))
    else:
        tic = pygame.transform.scale(pygame.image.load('images/o.png'), (TIC_SIZE, TIC_SIZE))
    text_rect = tic.get_rect(center=(x+2, y+2))
    screen.blit(tic, text_rect)
# Kiểm tra xem người chơi có thắng hay không
def check_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

#Vẽ lưới
def draw_grid():
    board = pygame.transform.scale(
            pygame.image.load('images/board.png'), (336, 336))
    board_x = 5
    board_y = 5
    
    screen.blit(board, (board_x, board_y))
    screen.blit(board, (board_x+336-6, board_y))
    

# Khởi tạo bảng và người chơi
num_rows = 10
num_cols = 10
board = [[0 for j in range(num_cols)] for i in range(num_rows)]
current_player = 1

# Vòng lặp chính của trò chơi
running = True
while running:
    # Xử lý sự kiện từ người dùng
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Lấy tọa độ của chuột khi người dùng click vào màn hình
            x, y = pygame.mouse.get_pos()
            # Tính toán vị trí của ô vuông tương ứng với tọa độ của chuột
            row = (y - MARGIN) // (SQUARE_SIZE + MARGIN)
            col = (x - MARGIN) // (SQUARE_SIZE + MARGIN)
            # Đặt ký hiệu 'X' hoặc 'O' vào ô vuông tương ứng và chuyển lượt cho người chơi khác
            if board[row][col] == 0:
                board[row][col] = current_player
                draw_xo(x, y, current_player)
                if check_win(board,current_player):
                    print(f"Player {current_player} wins!")
                    running = False
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

    # Cập nhật màn hình
    pygame.display.update()
# Kết thúc trò chơi và đóng cửa sổ
pygame.quit()
