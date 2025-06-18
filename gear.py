import pygame
from bullet import Bullet, KillBullet
import random as rnd

class Gear(): #Basic Single Shot
    def __init__(self,gearData:dict,isForEnemy: bool = False) -> None:
        self.bulletAmt = gearData["bulletAmt"]
        self.name = gearData["name"]
        self.radius = gearData["radius"]
        self.handleVelo(isForEnemy,gearData["velocity"])
        self.isEnemyGear = isForEnemy
        self.fireRate = gearData["fireRate"]
        self.dmg = gearData["damage"]
        self.pierce = gearData["pierce"]
        self.maxFire = self.fireRate - (self.fireRate * 0.75)
        spriteDict = gearData["bulletSprite"](isForEnemy)
        self.bulletSprite = (spriteDict["path"],spriteDict["width"],spriteDict["height"])
        self.fireFunc = gearData["fireFunc"]

    def handleVelo(self,isForEnemy: bool,bulletSpeed) -> None:
        if isForEnemy:
            self.velocity = [0,bulletSpeed]
        else:
            self.velocity = [0,bulletSpeed * -1]

    def getName(self) -> str:
        return self.name
    
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        return self.fireFunc(self,playerPosX,playerPosY,playerRad)
    
    def getFireRate(self) -> int:
        return self.fireRate
    
    def upgrade(self,tokenAmt) -> None:
        self.dmg += 1 if tokenAmt % 3 == 0 else 0
        self.fireRate -= 10 if tokenAmt % 5 == 0 and self.fireRate >= self.maxFire else 0