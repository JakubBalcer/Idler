
# PLAYER BĘDZIE W CAŁOŚCI SERIALIZOWANY ES
class Player:
    def __init__(self, resources):
        self.level = 0
        self.perks = []
        self.resources = resources
        self.items = []

    def add_perk(self, perk):
        self.perks.append(perk)

    def set_resources(self, resources):
        self.resources = resources
