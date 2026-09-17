'''
 # @ Author: Hugo Chartier
 # @ Create Time: 2026-09-10 17:28:04
 # @ Modified by: Hugo Chartier
 # @ Modified time: 2026-09-10 18:09:50
 # @ Description:
 '''
 
import os, warnings
from src.Point import Point
from src.Villager import Villager
from src.Carrot import Carrot
from pygame.surface import Surface
from pygame.time import Clock

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
 
import pygame, random

def main ():
    POPULATION : int = 10
    WIDTH : int = 1920
    HEIGH : int = 1080
    clock : Clock = Clock()
    win : Surface
    villagers : list[Villager]
    carrots : list[Carrot]
    
    win, villagers, carrots = init_interface(WIDTH, HEIGH, POPULATION)
    
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return pygame.quit()
        win.fill((0, 0 , 0))
        for villager in villagers:
            villager.drawVillager(win)
        for carrot in carrots:
            carrot.draw_carrot(win)
        pygame.display.flip()
 
def init_interface(pWidth : int, pHeight: int, pPopulation : int):
    villagers: list[Villager] = [] 
    carrots: list[Carrot] = []
    offset : int = 150
    i : int = 0
    win : Surface = None

    pygame.init()
    win = pygame.display.set_mode((pWidth, pHeight))
    while i < pPopulation:
        villagers.append(Villager(Point.getRandomPoint(pWidth, pHeight, offset)
            , (100, 200, 100)))
        carrots.append(Carrot(Point.getRandomPoint(pWidth, pHeight, offset)))
        i += 1
    return (win, villagers, carrots)

if __name__ == "__main__":
    main()