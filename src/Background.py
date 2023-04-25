import os
import GloDec as gd
import pygame as pg

class Background:

    def __init__(self, x):
        self.width = gd.WIDTH
        self.height = gd.HEIGHT
        self.x = x
        self.loadImage()
        self.show(gd.screen)

    def update(self, dx):
        self.x += dx
        if self.x <= -gd.WIDTH:
            self.x = gd.WIDTH

    def show(self, screen):
        screen.blit(self.image, (self.x, 0))
    
    def loadImage(self):
        path = os.path.join('src/images/bg.png')
        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image, (self.width, self.height))


    