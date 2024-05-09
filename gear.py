import pygame
from bullet import *
import random as rnd

class Gear(): #Basic Single Shot
    def __init__(self,isForEnemy: bool = False,bulletAmt: int = 1,radius:int = 5,fireRate: int = 200, damage: int = 1) -> None:
        self.bulletAmt = bulletAmt
        self.name = "Single Shot"
        self.radius = radius
        self.handleVelo(isForEnemy)
        self.isEnemyGear = isForEnemy
        self.fireRate = fireRate
        self.dmg = damage
        
    def handleVelo(self,isForEnemy: bool) -> None:
        if isForEnemy:
            self.velocity = [0,10]
        else:
            self.velocity = [0,-10]

    def getName(self) -> str:
        return self.name
    
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity)]
    
    def getFireRate(self) -> int:
        return self.fireRate
    

class DoubleShot(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,2,fireRate=400)
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
        super().__init__(isForEnemy,3,fireRate=400)
        self.name = "Triple Shot"
        
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        bulletList = []
        velocityX = -2
        velocityY = -10

        for i in range(self.bulletAmt):
            self.velocity = [velocityX,velocityY]
            bulletList.append(Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity))
            velocityX += 2
            
        return bulletList
    
class MachineGun(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,fireRate = 100)
        self.name = "Machine Gun"
        
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        velocityX = rnd.randint(-2,2)
        self.velocity[0] = velocityX
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity)]
                 
class HomingStrike(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,radius=10,fireRate = 600,damage=3)
        self.name = "Homing Strike"
        
    def getBulletList(self,playerPosX:float,playerPosY:float,playerRad:float,enemy) -> list:
        bulletList = []
        
        bulletList.append(HomingBullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,enemy))
            
        return bulletList