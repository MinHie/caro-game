import pygame

# Thiết lập kích thước cửa sổ và các màu sắc
WINDOW_SIZE = (600, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_COLOR = (128, 128, 128)

# Thiết lập kích thước và vị trí của mỗi ô vuông
SQUARE_SIZE = 100
MARGIN = 20
GRID_SIZE = SQUARE_SIZE * 3 + MARGIN * 4

# Thiết lập kích thước của đường kẻ
LINE_WIDTH = 10

# Khởi tạo màn hình
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Caro')

# Vẽ lưới trên màn hình
def draw_grid():
    for i in range(3):
        for j in range(3):
            x = MARGIN * (j + 1) + SQUARE_SIZE * j
            y = MARGIN * (i + 1) + SQUARE_SIZE * i
            pygame.draw.rect(screen, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(screen, LINE_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE), LINE_WIDTH)

# Vẽ ký hiệu 'X' hoặc 'O' trên màn hình
def draw_xo(x, y, player):
    font = pygame.font.SysFont(None, 200)
    if player == 1:
        text = font.render('X', True, BLACK)
    else:
        text = font.render('O', True, BLACK)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

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

# Khởi tạo bảng và người chơi
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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
    screen.fill(BLACK)
    draw_grid()
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                x = MARGIN * (j + 1) + SQUARE_SIZE * j + SQUARE_SIZE // 2
                y = MARGIN * (i + 1) + SQUARE_SIZE * i + SQUARE_SIZE // 2
                draw_xo(x, y, board[i][j])

    # Cập nhật màn hình
    pygame.display.update()

# Kết thúc trò chơi và đóng cửa sổ
pygame.quit()