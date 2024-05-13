import pygame
from bullet import *
from gear import *
from sprite import *
from enemy import *

class Player():
    
    def __init__(self,xpos:float,ypos:float,rad:int) -> None:
        self.x = xpos
        self.y = ypos
        self.rad = rad
        self.fireRate = 0
        self.playerColor = (0,0,0)
        self.health = 5
        self.totalBossTokens = 0
        self.gear = Gear()
        self.playerSprite = Sprite("sprites\PlayerShip.png",50,50)
        
    def movePlayer(self,amt:int) -> None:
        if self.x + amt < self.rad:
            self.x -= amt
        elif self.x + amt > 600 - self.rad:
            self.x -= amt
        else:
            self.x += amt
            
    def shoot(self,enemy:Enemy = None) -> list: #For Gear, Return a list
        if enemy == None:
            return self.gear.getBulletList(self.x,self.y,self.rad)
            
    def getScoreMultiplyer(self) -> None:
        return (self.totalBossTokens * 0.1) + 1

    def drawPlayer(self,screen:pygame.Surface) -> None:
        pygame.draw.circle(screen,self.playerColor,(self.x,self.y),self.rad,0)
        self.playerSprite.getImage(screen,(self.x - self.rad,self.y-self.rad))
       
    def getRad(self) -> float:
        return self.rad

    def getY(self) -> float:
        return self.y
    
    def getX(self) -> float:
        return self.x

