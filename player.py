import pygame
from bullet import *

class Player():
    
    def __init__(self,xpos,ypos,rad):
        self.x = xpos
        self.y = ypos
        self.rad = rad
        self.fireRate = 0
        self.playerColor = (0,0,255)
        self.health = 5
        self.totalBossTokens = 0
        
    def movePlayer(self,amt) -> None:
        if self.x + amt < self.rad:
            self.x -= amt
        elif self.x + amt > 600 - self.rad:
            self.x -= amt
        else:
            self.x += amt
            
    def shoot(self) -> Bullet:
        return Bullet(self.x,self.y - self.rad,5,10)
            
    def getScoreMultiplyer(self) -> None:
        return (self.totalBossTokens * 0.1) + 1

    def drawPlayer(self,screen) -> None:
        match(self.health):
            case 5:
                self.playerColor = (0,0,255)
            case 4:
                self.playerColor = (127,0,255)
            case 3:
                self.playerColor = (127,0,127)
            case 2:
                self.playerColor = (255,0,127)
            case 1:
                self.playerColor = (255,0,0)

        pygame.draw.circle(screen,self.playerColor,(self.x,self.y),self.rad,0)
       
    def getRad(self) -> float:
        return self.rad

    def getY(self) -> float:
        return self.y
    
    def getX(self) -> float:
        return self.x

