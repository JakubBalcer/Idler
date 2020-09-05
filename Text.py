import pygame

class Text:
    def __init__(self, text, font='arial', size=12, color=(255,255,255)):
        self.color = color
        self.text = text
        self.size = size
        self.font = pygame.font.match_font(font, self.size)
        self.bold = False
        self.italic = False
        self.pos = None

    def show(self, surface):
        # print(self.font)
        font = pygame.font.Font(self.font, self.size)
        surface.blit(font.render(self.text, True, self.color), self.pos)
        
    def setPos(self, pos):
        self.pos = pos