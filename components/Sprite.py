import pygame


class Sprite:
    def __init__(self, pos, size, src):
        self.pos = pos
        self.size = size
        self.src = src
        self.surface = pygame.transform.scale(
            pygame.image.load(self.src), self.size)
        self.visible = True
        self.destroyed = False

    def draw(self, surface):
        if self.visible:
            surface.blit(self.surface, self.pos)

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True
