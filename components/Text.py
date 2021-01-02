import pygame


class Text:
    def __init__(self, text, font='Centaur', size=16, color=(255, 255, 255)):
        self.color = color
        self.text = text
        self.size = size
        self.font = pygame.font.match_font(font, self.size)
        self.bold = False
        self.italic = False
        self.pos = None
        self.visible = True

    def draw(self, surface):
        # print(self.font)
        if self.visible:
            font = pygame.font.Font(self.font, self.size)
            surface.blit(font.render(self.text, True, self.color), self.pos)

    def setPos(self, pos):
        self.pos = pos

    def setText(self, text):
        self.text = text

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True
