from game_structures.Scene import Scene
from components.Constants import *
from components.Button import Button
from components.Counter import Counter
from components.Text import Text
from components.Sprite import Sprite


class Forest(Scene):
    def __init__(self, resources):
        super().__init__()
        self.resources = resources
        self.create_scene()

    def create_scene(self):
        wood_counter = Counter(self.rs_by_name("Wood"), size=32)
        wood_counter.setPos((10, 50))
        wood_counter.color = (255, 255, 255)
        wood_counter.set_prefix_text("Wood: ")
        self.components.append(wood_counter)

        money_counter = Counter(self.rs_by_name("Money"), size=32)
        money_counter.setPos((500, 50))
        money_counter.color = (255, 255, 255)
        money_counter.set_prefix_text("Money: $")
        self.components.append(money_counter)

        buttons = []
        b = Button((10, 100), (100, 100), True)
        b.setImage(OAK_LOG_IMG)
        b.setAction(lambda: wood_counter.increment(1))
        b.setBgcolor((131, 163, 161))
        b.setText("Chop wood!")
        self.components.append(b)

        money_btn = Button((500, 100), (100, 100), True)
        money_btn.setImage(SMALL_COIN_IMG)
        money_btn.setAction(
            lambda: money_counter.increment(wood_counter.empty()))
        money_btn.setBgcolor((131, 163, 161))
        money_btn.setText("Sell wood!")
        self.components.append(money_btn)

        text = Text("TEST")
        text.setPos((20, 40))
        text.color = (0, 0, 0)

        sprite = Sprite((100, 250), (100, 100), BASIC_AXE_IMG)
        self.components.append(sprite)

    def rs_by_name(self, name):
        return next(x for x in self.resources if x.name == name)
