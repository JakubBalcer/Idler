from components.Text import Text


class Input(Text):
    def __init__(self, textVal, font='Centaur', size=16, color=(255, 255, 255)):
        super().__init__("", font, size, color)
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False
