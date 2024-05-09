import pygame
from bullet import *
import random as rnd

class Gear(): #Basic Single Shot
    def __init__(self,isForEnemy: bool = False,bulletAmt: int = 1,radius:int = 5,fireRate: int = 200, damage: int = 1,pierce: int = 0,bulletSpeed: int = 10) -> None:
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
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.pierce)]
                 
class HomingStrike(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,radius=10,fireRate = 600,damage=3)
        self.name = "Homing Strike"
        
    def getBulletList(self,playerPosX:float,playerPosY:float,playerRad:float,enemy) -> list:
        return [HomingBullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,enemy)]
    
class Sniper(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,1,7,750,7,3,25)
        self.name = "Snipe"
        
    def getBulletList(self,playerPosX:float,playerPosY:float,playerRad:float) -> list:
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.pierce)]
        



