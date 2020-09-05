import pygame

class Button:
    def __init__(self, screen, x, y, size, shape):
        self.pos = self.x, self.y = x, y
        self.size = self.width, self.height = size
        self.shape = shape
        self.visible = True
        self.destroyed = False
        self.screen = screen

    def show(self):
        if self.visible:
            self.establish()

    def establish(self):
        if self.shape == 'rect':
            self.area = pygame.Rect(self.pos,self.size)
            pygame.draw.rect(self.screen, pygame.Color(255,255,255), self.area )

    def clicked(self, pos):
        if self.shape != 'ellipse':
            if self.area.collidepoint(pos):
                print("INSIDE")
            