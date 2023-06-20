class Button():
    def __init__(self, image, image_hover, pos):
        self.image = image
        self.image_hover = image_hover
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.hover = False

    def draw(self, screen):
        if self.hover:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.image_hover, self.rect)

    def check_click(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def check_hover(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.hover = True
        else:
            self.hover = False