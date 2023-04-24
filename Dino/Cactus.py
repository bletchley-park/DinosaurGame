import pygame as pg
import os
import GloDec as gd

class Cactus:

    def __init__(self, x):
        self.width = 34
        self.height = 44
        self.x = x
        self.y = 80
        self.loadImage()
        self.show(gd.screen)

    def update(self, dx):
        self.x += dx

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def loadImage(self):
        path = os.path.join('Dino/images/cactus.png')
        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image, (self.width, self.height))
