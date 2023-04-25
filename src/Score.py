import pygame as pg
import os
import GloDec as gd

class Score:
    def __init__(self, highScore):
        self.highScore = highScore
        self.currentScore = 0
        self.font = pg.font.SysFont('monospace', 18)
        self.color = "black"
        self.show()
        self.loadSound()
    
    def loadSound(self):
        path = os.path.join('src/sounds/point.wav')
        self.sound = pg.mixer.Sound(path)

    def update(self, score):
        self.currentScore = score
        self.highScore = max(self.currentScore, self.highScore)
        if(score % 100 == 0):
            if(score != 0):
                self.sound.play()

    def show(self):
        self.label = self.font.render(f"HI {self.highScore} {self.currentScore}", True, self.color)
        label_width = self.label.get_rect().width
        gd.screen.blit(self.label, (gd.WIDTH - label_width - 10, 10))
