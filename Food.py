import pygame
from colors import *
import random

class Food:
    def __init__(self, x,y, width, height, color = RED):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.pos = [x, y]
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.pos[0], self.pos[1], self.width, self.height))
    
    def randomize(self, width, height):
        self.pos = [random.randint(1, (width //self.width) - 1) * self.width, random.randint(1, (height//self.height) - 1) * self.height]
    