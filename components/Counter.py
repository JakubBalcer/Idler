import pygame
from game_structures.Resource import Resource
from components.Text import Text


class Counter(Text):
    def __init__(self, resource: Resource, font='Centaur', size=16, color=(255, 255, 255)):
        super().__init__(str(resource.amount), font, size, color)
        self.resource = resource
        self.per_second = 0
        self.prefix_text = ""

    def increment(self, amount=0):
        self.resource.amount += amount
        self.setText(self.prefix_text + str(self.resource.amount))

    def decrement(self, amount=0):
        self.resource.amount -= amount
        self.setText(self.prefix_text + str(self.resource.amount))

    def mult(self, amount=1):
        self.resource.amount *= amount
        self.setText(self.prefix_text + str(self.resource.amount))

    def div(self, amount=1):
        self.resource.amount /= amount
        self.setText(self.prefix_text + str(self.resource.amount))

    def setValue(self, value=0):
        self.resource.amount = value
        self.setText(self.prefix_text + str(self.resource.amount))

    def customAction(self, action):
        self.resource.amount = action()
        self.setText(self.prefix_text + str(self.resource.amount))

    def each_second(self):
        self.increment(self.per_second)
        self.setText(self.prefix_text + str(self.resource.amount))

    def add_to_ps(self, amount):
        self.per_second += amount

    def set_prefix_text(self, text):
        self.prefix_text = text
        self.text = self.prefix_text + self.text

    def empty(self):
        val = self.resource.amount
        self.setValue()
        return val

    def get_save_data(self):
        pass
