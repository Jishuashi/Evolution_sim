'''
 # @ Author: Hugo Chartier
 # @ Create Time: 2026-09-10 17:28:04
 # @ Modified by: Hugo Chartier
 # @ Modified time: 2026-09-10 18:09:50
 # @ Description:
 '''
 
import os, warnings

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
 
import pygame, random

def main ():
    POPULATION = 10
    WIDTH = 600
    HEIGH = 600
    clock = pygame.time.Clock()
    windows = init_interface(WIDTH, HEIGH)
    
    clock.tick(60)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
 
def init_interface(pWidth, pHeight):
    pygame.init()
    return pygame.display.set_mode((pWidth, pHeight))

if __name__ == "__main__":
    main()