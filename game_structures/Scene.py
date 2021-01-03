class Scene:
    def __init__(self):
        self.components = []

    def draw(self, surface):
        for component in self.components:
            component.draw(surface)
