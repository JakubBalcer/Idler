import pygame
from components.Sprite import Sprite
from components.Text import Text

# TO DO
# BOUND TEXT INSIDE BUTTON
# CENTERING TEXT INSIDE BUTTON


class Button:
    def __init__(self, pos, size, background=True):
        self.pos = self.x, self.y = pos
        self.size = self.width, self.height = size
        self.background = background
        self.visible = True
        self.destroyed = False
        self.action = None
        self.text = None
        self.image = None
        self.bgcolor = 0, 0, 0
        self.active = True

    def draw(self, surface):
        if self.visible:
            self.establish(surface)
            self.renderText(surface)
            if self.image:
                self.image.draw(surface)

    def establish(self, surface):
        self.area = pygame.Rect(self.pos, self.size)
        if self.background:
            pygame.draw.rect(surface, pygame.Color(*self.bgcolor), self.area)

    def clicked(self, pos):
        if self.area.collidepoint(pos) and self.active:
            self.dispatchAction()

    def setAction(self, action):
        self.action = action

    def renderText(self, surface):
        if self.text:
            self.text.setPos(self.pos)
            self.text.draw(surface)

    def dispatchAction(self, action=None):
        try:
            if self.action:
                self.action()
            elif action:
                action()
            else:
                raise Exception("Missing action")
        except:
            print("EXCEPTION: Missing action")

    def setText(self, text):
        if type(text) is Text:
            self.text = text

        if type(text) is str:
            self.text = Text(text)

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True

    def setImage(self, imageUrl):
        self.image = Sprite(self.pos, self.size, imageUrl)

    def setBgcolor(self, color):
        self.bgcolor = color

    def set_active(self, active):
        self.active = active
