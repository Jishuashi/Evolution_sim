'''
 # @ Author: Hugo Chartier
 # @ Create Time: 2026-09-11 18:24:33
 # @ Modified by: Hugo Chartier
 # @ Modified time: 2026-09-11 18:24:35
 # @ Description:
 '''

import pygame, math, random
from src.entities.Point import Point
from src.entities.Carrot import Carrot
from pygame.surface import Surface
from src.const import *

class Villager:
    def __init__(self, pPos : Point, pColor : tuple, pSize : float):
        self._pos : Point = pPos
        self._color : tuple = pColor
        self._size : float = pSize
        self._alive : bool = True
        self._energy : float = (INITIAL_ENERGY * math.pow(self._size, ENERGY_SIZE_EXPONENT))
        self._max_energy : int = self._energy
        self._max_speed : int = (INTIAL_SPEED / self._size)
        self._speed : float = 0
        self._angle : float = random.uniform(0, 2*math.pi)
        
    def drawVillager(self, pWin : Surface) -> None:
        if (self._alive):
            pygame.draw.circle(pWin, self._color, self._pos.getPoint()
                , (INITIAL_VILLAGER_RADIUS * self._size))

    def getPos(self) -> Point:
        return self._pos
    
    def setPos(self, pPos: Point) -> None:
        self._pos = pPos
        
    def getColor(self) -> tuple:
        return self._color
    
    def setColor(self, pColor : tuple) -> None:
        self._color = pColor
       
    def move(self, pAngle : int) -> None:
        posX = self._pos.getX()
        posY = self._pos.getY()
        
        self._speed = random.uniform(0, self._max_speed)
        
        newPosX = posX + (math.cos(pAngle) * self._speed)
        newPosY = posY + (math.sin(pAngle) * self._speed)
        
        if (newPosX >= WIDTH):
            newPosX = WIDTH
        elif (newPosX <= 0):
            newPosX = 0

        if (newPosY >= HEIGH):
            newPosY = HEIGH
        elif (newPosY <= 0):
            newPosY = 0
        self._pos.setPoint(newPosX, newPosY)

    def update(self, pCarrots: list[Carrot]) -> None:
        if (self._alive):
            for carrot in pCarrots:
                  dist = self.getPos().getDistance(carrot.getPos())
                  if (dist <= ((self._size * INITIAL_VILLAGER_RADIUS) + CARROT_RADIUS)
                        and (not carrot.getIfEated())):
                      self._energy = min(self._energy + (INITIAL_ENERGY * 0.1), self._max_energy)
                      carrot.eated()
            self._angle += random.uniform(-0.1, 0.1);
            self.move(self._angle)
            self._energy -= self._size * (METABOLISM_COST + MOVE_COST * self._speed)

        if(self._energy <= 0):
            self._alive = False