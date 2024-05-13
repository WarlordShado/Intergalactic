import pygame
from bullet import *
import random as rnd

class Gear(): #Basic Single Shot
    def __init__(self,isForEnemy: bool = False,bulletAmt: int = 1,radius:int = 5,fireRate: int = 200, damage: int = 3,pierce: int = 0,bulletSpeed: int = 10) -> None:
        self.bulletAmt = bulletAmt
        self.name = "Single Shot"
        self.radius = radius
        self.handleVelo(isForEnemy,bulletSpeed)
        self.isEnemyGear = isForEnemy
        self.fireRate = fireRate
        self.dmg = damage
        self.pierce = pierce
        
    def handleVelo(self,isForEnemy: bool,bulletSpeed) -> None:
        if isForEnemy:
            self.velocity = [0,bulletSpeed]
        else:
            self.velocity = [0,bulletSpeed * -1]

    def getName(self) -> str:
        return self.name
    
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity)]
    
    def getFireRate(self) -> int:
        return self.fireRate
    

class DoubleShot(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,2,fireRate=400,damage=2)
        self.name = "Double Shot"
        self.bulletSpacing = 20
        
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        bulletList = []
        playerPosX -= self.bulletSpacing//2

        for i in range(self.bulletAmt):
            bulletList.append(Bullet(playerPosX + (i * self.bulletSpacing),playerPosY - playerRad,self.radius,self.velocity))
            
        return bulletList
        
class TripleShot(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,3,fireRate=425,damage=2)
        self.name = "Triple Shot"
        
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        bulletList = []
        velocityX = -2
        if self.isEnemyGear:
            velocityY = 10
        else:
            velocityY = -10

        for i in range(self.bulletAmt):
            self.velocity = [velocityX,velocityY]
            bulletList.append(Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity))
            velocityX += 2
            
        return bulletList
    
class MachineGun(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,2,fireRate = 125,damage=1)
        self.name = "Machine Gun"
        
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        bulletList = []

        for i in range(self.bulletAmt):
            velocityX = rnd.uniform(-2,2)
            self.velocity = [velocityX,-10]
            bulletList.append(Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.pierce))

        return bulletList
    
class Sniper(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,1,7,900,7,2,25)
        self.name = "Sniper"
        
    def getBulletList(self,playerPosX:float,playerPosY:float,playerRad:float) -> list:
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.pierce,True)]
    
class BlackHole(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,1,15,1500,10,10,3)
        self.name = "Black Hole"
        
    def getBulletList(self,playerPosX:float,playerPosY:float,playerRad:float) -> list:
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.pierce)]
        



