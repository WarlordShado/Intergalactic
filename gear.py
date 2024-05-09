import pygame
from bullet import *
import random as rnd

class Gear(): #Basic Single Shot
    def __init__(self,isForEnemy: bool = False) -> None:
        self.bulletAmt = 1
        self.name = "Single Shot"
        self.radius = 5
        self.handleVelo(isForEnemy)
        self.isEnemyGear = isForEnemy
        self.fireRate = 200
        self.dmg = 1
        
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
        super().__init__(isForEnemy)
        self.bulletAmt = 2
        self.name = "Double Shot"
        self.bulletSpacing = 20
        self.fireRate = 400
        
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        bulletList = []
        playerPosX -= self.bulletSpacing//2

        for i in range(self.bulletAmt):
            bulletList.append(Bullet(playerPosX + (i * self.bulletSpacing),playerPosY - playerRad,self.radius,self.velocity))
            
        return bulletList
        
class TripleShot(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy)
        self.bulletAmt = 3
        self.name = "Triple Shot"
        self.fireRate = 400
        
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        bulletList = []
        velocityX = 2

        for i in range(self.bulletAmt):
            self.velocity[0] = velocityX
            bulletList.append(Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity))
            velocityX -= 2
            
        return bulletList
    
class MachineGun(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy)
        self.bulletAmt = 3
        self.name = "Machine Gun"
        self.fireRate = 100
        
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        velocityX = rnd.randint(-2,2)
        self.velocity[0] = velocityX
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity)]
                 
class HomingStrike(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy)
        self.bulletAmt = 1
        self.name = "Homing Strike"
        self.fireRate = 600
        self.radius = 10
        self.dmg = 3
        
    def getBulletList(self,playerPosX:float,playerPosY:float,playerRad:float,enemy) -> list:
        bulletList = []
        
        bulletList.append(HomingBullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,enemy))
            
        return bulletList