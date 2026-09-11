'''
 # @ Author: Hugo Chartier
 # @ Create Time: 2026-09-11 18:24:33
 # @ Modified by: Hugo Chartier
 # @ Modified time: 2026-09-11 18:24:35
 # @ Description:
 '''

import pygame
from src.Point import Point
from pygame.surface import Surface

class Villager:
    def __init__(self, pPos : Point, pColor : tuple):
        self._pos : Point = pPos
        self._color : tuple = pColor
        
    def drawVillager(self, pWin : Surface):
        pygame.draw.circle(pWin, self._color, self._pos.getPoint(), 10)

    def getPos(self) -> Point:
        return self._pos
    
    def setPos(self, pPos):
        self._pos = pPos
        
    def getColor(self)  -> tuple:
        return self._color
    
    def setColor(self, pColor):
        self._color = pColor