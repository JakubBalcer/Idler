from game_structures.Scene import Scene
from components.Constants import *
from components.Button import Button
from components.Counter import Counter
from components.Text import Text
from components.Sprite import Sprite


class General(Scene):
    def __init__(self, resources, stage):
        super().__init__(stage)
        self.resources = resources
        self.create_scene()

    def create_scene(self):
        text = Text("GENERAL")
        text.setPos((100, 100))
        self.components.append(text)
