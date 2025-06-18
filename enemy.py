import pygame
from sprite import Sprite
from bullet import Bullet, KillBullet
from gear import Gear
from gameData.gearData import *
from random import randint as rnd

ROUND_MOD = 5

class Enemy():
    def __init__(self,xPos:float,yPos:float,rad:int,data:dict,round:int = 1) -> None:
        self.x = xPos
        self.y = yPos
        self.rad = rad
        self.speed = data["speed"]
        self.hasCoin = data["coinOdds"]()
        self.gear = Gear(GEAR_DATA[data["gear"]],True)
        self.fireRate = data["fireRate"]
        self.enemySprite = Sprite(data["sprite"]["path"],data["sprite"]["width"],data["sprite"]["height"])
        self.health = data["hp"](round)
        self.scoreVal = data["scoreVal"]
        
    def drawEnemy(self,screen:pygame.Surface) -> None:
        hitboxSurface = pygame.Surface((self.x - self.rad,self.y-self.rad))
        hitboxSurface.set_colorkey((0,0,0))
        hitboxSurface.set_alpha(0)
        pygame.draw.circle(hitboxSurface,(0,0,0),(self.x,self.y),self.rad,0)
        self.enemySprite.getImage(screen,(self.x - self.rad,self.y - self.rad))
        screen.blit(hitboxSurface,(self.x - self.rad,self.y-self.rad))
        
    def moveEnemy(self) -> None:
        self.x += self.speed
            
    def shoot(self) -> Bullet:
        return self.gear.getBulletList(self.x,self.y,self.rad)

    def reverseSpeed(self) -> None:
        self.speed *= -1

    def getRad(self) -> float:
        return self.rad

    def getX(self) -> float:
        return self.x
    
    def getY(self) -> float:
        return self.y
    
class Boss(Enemy): #Used as a Structure for inheritance
    def __init__(self,xPos:float,yPos:float,rad:int,data:dict,round:int = 1) -> None:
        super().__init__(xPos,yPos,rad,data,round)
        self.maxHp = data["maxHp"](round)
        self.color = (0,0,0)
        self.name = data["name"]
        self.specRate = data["specRate"]
        self.canBeHurtFunc = data["can_be_hurt"]
        self.spec = data["special"]
        
    def canBeHurt(self) -> bool:
        return self.canBeHurtFunc(self)
    
    def special(self):
        return self.spec(self)
    
    def getName(self) -> str:
        return self.name