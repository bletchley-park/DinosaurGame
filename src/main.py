import pygame as pg
from sys import exit
import math
import random

import GloDec as gd
import Game

pg.init()
pg.mixer.init()
pg.display.set_caption('Dinosaur Game')

def main():
    game = Game.Game()
    dinosaur = game.dinosaur

    time = 0

    gameover = False

    clock = pg.time.Clock()

    while True:
        if game.playing:
            for background in game.backgrounds:
                background.update(-game.speed)
                background.show(gd.screen)

            dinosaur.update(time)
            dinosaur.show(gd.screen)
            
            if game.toSpawn(time):
                game.spawn()

            for cactus in game.obstacles:
                cactus.update(-game.speed)
                cactus.show(gd.screen)

                if(math.hypot(cactus.x - dinosaur.x, cactus.y - dinosaur.y) < 35):
                    gameover = True  

            if gameover:
                game.endGame()
                gameover = False

            game.score.update(time // 10)
            game.score.show()         
            
            
            time += 1 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()     
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:  
                    if not game.playing:
                        game.restartGame()
                        game.startGame()
                        time = 0
                    else:
                        if dinosaur.onGround:
                            dinosaur.jump()
                    
                    



        pg.display.update()
        clock.tick(60)


main()