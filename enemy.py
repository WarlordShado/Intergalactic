import pygame
from bullet import *

class Enemy():
    def __init__(self,xPos:float,yPos:float,rad:int,hasCoin:bool):
        self.x = xPos
        self.y = yPos
        self.rad = rad
        self.speed = 5
        self.hasCoin = hasCoin
        
    def drawEnemy(self,screen:pygame.Surface) -> None:
        pygame.draw.circle(screen,(255,0,0),(self.x,self.y),self.rad,0)
        
    def moveEnemy(self) -> None:
        if self.x + self.speed < self.rad:
            self.x -= self.speed
        elif self.x + self.speed > 600 - self.rad:
            self.x -= self.speed
        else:
            self.x += self.speed
            
    def shoot(self) -> Bullet:
        return Bullet(self.x,self.y + self.rad,5,(0,10))

    def reverseSpeed(self) -> None:
        self.speed *= -1

    def getRad(self) -> float:
        return self.rad

    def getX(self) -> float:
        return self.x
    
    def getY(self) -> float:
        return self.y
    
class Boss(Enemy):
    def __init__(self,xPos:float,yPos:float,rad:int):
        super().__init__(xPos,yPos,rad,True)
        self.health = 30
        self.color = (255,0,0)
        self.minionList = []
        
    def drawEnemy(self,screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.rad,0)
        
    def makeMinions(self,screen: pygame.Surface) -> None:
        for i in range(1,6):
            self.minionList.append(Minion(100 * i + 1,175,15))
        
    def changeColor(self) -> None:
        if self.health // 5 == 5:
            self.color = (255,0,127)
        elif self.health // 5 == 4:
            self.color = (127,0,127)
        elif self.health // 5 == 3:
            self.color = (0,0,127)
        elif self.health // 5 == 2:
            self.color = (127,0,255) 
        elif self.health // 5 == 1:
            self.color = (0,0,255)
            
class Minion(Boss): #Boss Minion, They can't move
    def __init__(self,xPos: float,yPos: float,rad: int):
        super().__init__(xPos,yPos,rad)
        self.health = 3
        
    def changeColor(self) -> None:
        if self.health == 3:
            self.color = (34,132,34)
        elif self.health == 2:
            self.color = (50,205,50) 
        elif self.health == 1:
            self.color = (125,251,125)