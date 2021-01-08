from components.Button import Button
import json


class Scene:
    def __init__(self, stage):
        self.components = []
        self.stage = stage
        self.set_main_menu()

    def draw(self, surface):
        for component in self.components:
            component.draw(surface)

    def set_main_menu(self):
        with open("tabs.json") as file:
            data = json.load(file)
            i = 0
            for tab in data['tabs']:
                self.components.append(Button((i*110, 5), (100, 30)))
                self.components[i].setText(tab)
                self.components[i].setAction(
                    lambda tab=tab: self.stage.set_scene(tab))
                i += 1
