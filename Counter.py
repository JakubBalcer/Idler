import pygame
from Text import Text

class Counter(Text):
    def __init__(self, text, font='arial', size=12, color=(255,255,255)):
        super().__init__(text, font, size, color)

    def increment(self, amount=1):
        temp = int(self.text)
        temp += amount
        self.text = str(temp)

    def decrement(self, amount=1):
        temp = int(self.text)
        temp -= amount
        self.text = str(temp)

    def mult(self, amount=1):
        temp = int(self.text)
        temp *= amount
        self.text = str(temp)

    def div(self, amount=1):
        temp = int(self.text)
        temp /= amount
        self.text = str(temp)

    def setValue(self, value=0):
        temp = int(self.text)
        temp = value
        self.text = str(temp)