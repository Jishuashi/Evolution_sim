'''
 # @ Author: Hugo Chartier
 # @ Create Time: 2026-09-11 17:21:13
 # @ Modified by: Hugo Chartier
 # @ Modified time: 2026-09-11 17:24:28
 # @ Description:
 '''

import random

class Point:
    def __init__(self, pX, pY):
        self._x = pX
        self._y = pY
        
    def getPoint(self):
        return (float(self._x), float(self._y)) 
    
    def setPoint(self, pX, pY):
        self._x = pX
        self._y = pY
    
    def getX(self) -> float:
        return self._x
    
    def getY(self) -> float:
        return self._y
    
    @staticmethod
    def getRandomPoint(pXMax : int, pYMax: int, pOffset : int):
        point = Point(random.randint(pOffset, (pXMax - pOffset))
                    , random.randint(pOffset, (pYMax - pOffset)))
        return point
    