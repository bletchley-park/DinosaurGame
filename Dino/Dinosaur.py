import pygame as pg
import os
import GloDec as gd

class Dinosaur:

    def __init__(self):
        self.width = 44
        self.height = 44
        self.x = 10
        self.y = 80
        self.imageNum = 0
        self.dy = 3
        self.onGround = True
        self.jumping = False
        self.jumpStop = 10
        self.falling = False
        self.fallStop = self.y
        self.loadImage()
        self.loadSound()
        self.show(gd.screen)

    def update(self, time):
        if self.jumping:
            self.y -= self.dy
            #self.dy -= 3/70
            if self.y <= self.jumpStop:
                self.fall()     
                #print(time)   
        elif self.falling:
            self.y += self.dy
            #self.dy += 3/70
            if self.y >= self.fallStop:
                self.stop()
                #print(time)
        elif self.onGround and time % 4 == 0:
            self.imageNum = (self.imageNum + 1) % 3
            self.loadImage()
        # if self.jumping:
        #     self.y -= self.dy
        #     if self.y <= self.jumpStop:
        #         self.fall()        
        # elif self.falling:
        #     self.y += self.dy
        #     if self.y >= self.fallStop:
        #         self.stop()
        # elif self.onGround and time % 4 == 0:
        #     self.imageNum = (self.imageNum + 1) % 3
        #     self.loadImage()

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def loadImage(self):
        path = os.path.join(f'Dino/images/dino{self.imageNum}.png')
        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image, (self.width, self.height))

    def loadSound(self):
        path = os.path.join('Dino/sounds/jump.wav')
        self.sound = pg.mixer.Sound(path)

    def jump(self):
        self.sound.play()
        self.jumping = True
        self.onGround = False

    def fall(self):
        self.jumping = False
        self.falling = True

    def stop(self):
        self.falling = False
        self.onGround = True