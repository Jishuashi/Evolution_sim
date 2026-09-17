'''
 # @ Author: Hugo Chartier
 # @ Create Time: 2026-09-11 18:50:38
 # @ Modified by: Hugo Chartier
 # @ Modified time: 2026-09-11 18:50:40
 # @ Description:
 '''

import pygame
from pygame.surface import Surface
from src.Point import Point

class Carrot:
    def __init__(self, pPos : Point):
        self._pos : Point = pPos
        pass
    
    def draw_carrot(self, pWin: Surface):
        ORANGE : tuple = (230, 140, 40)
        GREEN : tuple = (90, 170, 80)
        x : float = self._pos.getX()
        y : float = self._pos.getY()

        body = [(x - 4.2, y - 7), (x + 4.2, y - 7), (x, y + 9.8)]
        pygame.draw.polygon(pWin, ORANGE, body)
        pygame.draw.line(pWin, (200, 110, 20), (x - 1.4, y - 4.2), (x - 0.7, y + 5.6), 1)
        pygame.draw.line(pWin, (200, 110, 20), (x + 1.4, y - 4.2), (x + 0.7, y + 5.6), 1)
        for dx in (-3.5, 0, 3.5):
            leaf = [(x, y - 7), (x + dx - 2.1, y - 14), (x + dx + 2.1, y - 14)]
            pygame.draw.polygon(pWin, GREEN, leaf)

    def getPos(self) -> Point:
            return self._pos
        
    def setPos(self, pPos):
        self._pos = pPos