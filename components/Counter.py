import pygame
from components.Text import Text


class Counter(Text):
    def __init__(self, value: float, font='Centaur', size=16, color=(255, 255, 255)):
        super().__init__(str(value), font, size, color)
        self.value = value
        self.per_second = 0
        self.prefix_text = ""

    def increment(self, amount=0):
        self.value += amount
        self.text = self.prefix_text + str(self.value)

    def decrement(self, amount=0):
        self.value -= amount
        self.text = self.prefix_text + str(self.value)

    def mult(self, amount=1):
        self.value *= amount
        self.text = self.prefix_text + str(self.value)

    def div(self, amount=1):
        self.value /= amount
        self.text = self.prefix_text + str(self.value)

    def setValue(self, value=0):
        self.value = value
        self.text = self.prefix_text + str(self.value)

    def customAction(self, action):
        self.value = action()
        self.text = self.prefix_text + str(self.value)

    def each_second(self):
        self.increment(self.per_second)
        self.text = self.prefix_text + str(self.value)

    def add_to_ps(self, amount):
        self.per_second += amount

    def set_prefix_text(self, text):
        self.prefix_text = text
        self.text = self.prefix_text + self.text

    def empty(self):
        val = self.value
        self.setValue()
        return val
