from scenes.Forest import Forest
from scenes.General import General


class Stage:
    def __init__(self, resources):
        self.resources = resources
        self.scenes = {"Forest": Forest(
            self.rs_by_tab("Forest"), self), "General": General(None, self)}
        self.current_scene = None

    def set_scene(self, tab_name):
        self.current_scene = self.scenes[tab_name]

    def draw_scene(self, surface):
        if self.current_scene:
            self.current_scene.draw(surface)

    def rs_by_tab(self, tab_name):
        return filter(lambda resource: resource.tab == tab_name, self.resources)

    def get_components(self):
        return self.current_scene.components

    def add_component(self, component):
        self.current_scene.components.append(component)
