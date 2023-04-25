import Background
import Dinosaur
import Cactus
import Score
import GloDec as gd
import pygame as pg
import random
import os

class Game:

    def __init__(self, hs = 0):
        self.backgrounds = [Background.Background(0), Background.Background(gd.WIDTH)]
        self.dinosaur = Dinosaur.Dinosaur()
        self.obstacles = []
        self.speed = 3
        self.score = Score.Score(hs)
        self.playing = False
        self.loadSound()
        self.writeLabels()
    
    def loadSound(self):
        path = os.path.join('src/sounds/die.wav')
        self.sound = pg.mixer.Sound(path)
    
    def writeLabels(self):
        bigFont = pg.font.SysFont('monospace', 24, bold = True)
        smallFont = pg.font.SysFont('monospace', 18)
        self.bigLabel = bigFont.render(f'G A M E  O V E R', 1, (0, 0, 0))
        self.smallLabel = smallFont.render(f'press SPACE to restart', 1, (0, 0, 0))
    
    def startGame(self):
        self.playing = True

    def endGame(self):
        self.sound.play()
        gd.screen.blit(self.bigLabel, (gd.WIDTH // 2 - self.bigLabel.get_width() // 2, gd.HEIGHT // 4))
        gd.screen.blit(self.smallLabel, (gd.WIDTH // 2 - self.smallLabel.get_width() // 2, gd.HEIGHT // 2))
        self.playing = False

    def restartGame(self):
        self.__init__(self.score.highScore)
    
    def toSpawn(self, loops):
        return loops % 100 == 0
    
    def spawn(self):
        x = 0

        if len(self.obstacles) > 0:
            pos = self.obstacles[-1].x + 44 + 84
            x = random.randint(pos, gd.WIDTH + pos)
        else:
            x = random.randint(100 + gd.WIDTH, 1000)

        self.obstacles.append(Cactus.Cactus(x))


