import pygame
from pygame.locals import *
import sys
import os
import time
width = 950
height = 500
timer = 0
Screen = 2 # 1 = Main screen | 2 = Game screen | 3 = Game Over screen

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Dog')
    background = pygame.image.load(os.path.join("Images", "Background_00.png")).convert()
    FlappyDog = pygame.image.load(os.path.join("Images", "Flappy.png")).convert_alpha()
    Play = pygame.image.load(os.path.join("Images", "Play.png")).convert_alpha()
    Dog0 = pygame.image.load(os.path.join("Images", "Dog0.png")).convert_alpha()
    Dog1 = pygame.image.load(os.path.join("Images", "Dog1.png")).convert_alpha()
    SpikeUp0 = pygame.image.load(os.path.join("Images", "SpikeUp0.png")).convert_alpha()
    SpikeUp1 = pygame.image.load(os.path.join("Images", "SpikeUp1.png")).convert_alpha()
    SpikeDown0 = pygame.image.load(os.path.join("Images", "SpikeDown0.png")).convert_alpha()
    SpikeDown1 = pygame.image.load(os.path.join("Images", "SpikeDown1.png")).convert_alpha()
    GameOver = pygame.image.load(os.path.join("Images", "Game-Over.png")).convert_alpha()
    Replay = pygame.image.load(os.path.join("Images", "Replay.png")).convert_alpha()
    Drop = pygame.image.load(os.path.join("Images", "Drop.png")).convert_alpha()
    Bone = pygame.image.load(os.path.join("Images", "Bone.png")).convert_alpha()
    if Screen == 1:
        screen.blit(background, (0, 0))
        screen.blit(FlappyDog, (0, 0))
        screen.blit(Drop, (750, 20))
        screen.blit(Bone, (550, 100))
        screen.blit(Play, (600, 350))
        screen.blit(Dog0, (5, 240))
        pygame.display.update()
        mouse = pygame.mouse.get_pos()

    if Screen == 2:
        screen.blit(background, (0, 0))
        screen.blit(Dog1, (0, 0))
        pygame.display.update()
    while True:
        if Screen == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
                   pygame.display.update()

    if  Screen == 0:
        screen.blit(background, (0, 0))
        screen.blit(Dog1, (0, 0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    pygame.display.update()
    while Screen == 2:
        wait(1)
        timer = timer +1
        print (timer)
        

if __name__ == "__main__":
    main()
