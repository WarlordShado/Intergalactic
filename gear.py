import pygame
from bullet import *
import random as rnd

class Gear(): #Basic Single Shot
    def __init__(self) -> None:
        self.bulletAmt = 1
        self.name = "Single Shot"
        self.radius = 5
        self.velocity = [0,-10]
        self.fireRate = 300
        
    def getName(self) -> str:
        return self.name
    
    def getBulletList(self, playerPosX,playerPosY,playerRad) -> list:
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity)]
    
    def getFireRate(self) -> int:
        return self.fireRate
    

class DoubleShot(Gear):
    def __init__(self) -> None:
        super().__init__()
        self.bulletAmt = 2
        self.name = "Double Shot"
        self.bulletSpacing = 20
        self.fireRate = 400
        
    def getBulletList(self, playerPosX,playerPosY,playerRad) -> list:
        bulletList = []
        playerPosX -= self.bulletSpacing//2

        for i in range(self.bulletAmt):
            bulletList.append(Bullet(playerPosX + (i * self.bulletSpacing),playerPosY - playerRad,self.radius,self.velocity))
            
        return bulletList
        
class TripleShot(Gear):
    def __init__(self) -> None:
        super().__init__()
        self.bulletAmt = 3
        self.name = "Triple Shot"
        self.fireRate = 400
        
    def getBulletList(self, playerPosX,playerPosY,playerRad) -> list:
        bulletList = []
        velocityX = 2

        for i in range(self.bulletAmt):
            bulletList.append(Bullet(playerPosX,playerPosY - playerRad,self.radius,[velocityX,-10]))
            velocityX -= 2
            
        return bulletList
    
class MachineGun(Gear):
    def __init__(self) -> None:
        super().__init__()
        self.bulletAmt = 3
        self.name = "Machine Gun"
        self.fireRate = 100
        
    def getBulletList(self, playerPosX,playerPosY,playerRad) -> list:
        velocityX = rnd.randint(-2,2)

        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,[velocityX,-10])]
        
            
        