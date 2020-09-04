import pygame
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import matplotlib.path as mplPath
import numpy as np

class Button:
    def __init__(self, screen, x, y, size, shape):
        self.pos = self.x, self.y = x, y
        self.size = self.width, self.height = size
        self.shape = shape
        self.visible = True
        self.destroyed = False
        self.screen = screen
        self.pol = Polygon([self.pos, (self.x+self.width, self.y), (self.x, self.y+self.height), (self.x+self.width, self.y + self.height) ])
        pass

    def show(self):
        if self.visible:
            self.establish()

    def establish(self):
        if self.shape == 'rect':
            pygame.draw.rect(self.screen, pygame.Color(255,255,255), pygame.Rect(self.pos,self.size))

    def clicked(self, pos):
        pt = Point(pos)
        
        print(self.pol)
        print(pt)
        if self.shape != 'ellipse':
            if self.pol.contains(pt):
                print("INSIDE")