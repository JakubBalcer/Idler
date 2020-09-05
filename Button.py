import pygame

# TO DO 
# BOUND TEXT INSIDE BUTTON
# CENTERING TEXT INSIDE BUTTON
# SET IMAGE INSIDE BUTTON

class Button:
    def __init__(self, x, y, size, shape):
        self.pos = self.x, self.y = x, y
        self.size = self.width, self.height = size
        self.shape = shape
        self.visible = True
        self.destroyed = False
        self.action = None
        self.text = None

    def show(self, surface):
        if self.visible:
            self.establish(surface)
            if self.text:
                self.renderText(surface)


    def establish(self, surface):
        if self.shape == 'rect':
            self.area = pygame.Rect(self.pos,self.size)
            pygame.draw.rect(surface, pygame.Color(255,255,255), self.area )

    def clicked(self, pos):
        if self.shape != 'ellipse':
            if self.area.collidepoint(pos):
                self.dispatchAction()

    def setAction(self, action):
        self.action = action

    def renderText(self, surface):
        self.text.setPos(self.pos)
        self.text.show(surface)
            
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
        self.text = text

