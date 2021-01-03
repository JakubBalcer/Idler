from components.Button import Button


class Tab(Button):
    def __init__(self, name, pos, size):
        super().__init__(pos, size)
        self.name = name
        self.active = False
        self.setText(self.name)

    def __str__(self):
        return self.name

    def set_active(self, active):
        self.active = active
