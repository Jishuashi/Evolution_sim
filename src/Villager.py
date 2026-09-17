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
    def __init__(self, pPos : Point, pColor : tuple, pSize : float):
        self._pos : Point = pPos
        self._color : tuple = pColor
        self._size : float = pSize
        self._alive : bool = True
        self._energy : float = (300.0 * self._size)
        self._speed : float = (1.0 / self._size)
        
    def drawVillager(self, pWin : Surface):
        if (self._alive):
            pygame.draw.circle(pWin, self._color, self._pos.getPoint(), (8 * self._size))

    def getPos(self) -> Point:
        return self._pos
    
    def setPos(self, pPos):
        self._pos = pPos
        
    def getColor(self)  -> tuple:
        return self._color
    
    def setColor(self, pColor):
        self._color = pColor
        
    def update(self):
        if (self._alive):
            self._energy -= 1
        if(self._energy <= 0):
            self._alive = False