import pygame
from bullet import Bullet, KillBullet
import random as rnd

#FIX BULLET SPRITES!!!!!!!!!!!!!!!

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
        self.maxFire = fireRate - (fireRate * 0.75)
        self.bulletSprite = ("sprites\BasicBullet.png",10,10) if not isForEnemy else ("sprites\EnemyBullet.png",10,10)
        
    def handleVelo(self,isForEnemy: bool,bulletSpeed) -> None:
        if isForEnemy:
            self.velocity = [0,bulletSpeed]
        else:
            self.velocity = [0,bulletSpeed * -1]

    def getName(self) -> str:
        return self.name
    
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite)]
    
    def getFireRate(self) -> int:
        return self.fireRate
    
    def upgrade(self,tokenAmt) -> None:
        self.dmg += 1 if tokenAmt % 3 == 0 else 0
        self.fireRate -= 10 if tokenAmt % 5 == 0 and self.fireRate >= self.maxFire else 0

class DoubleShot(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,2,fireRate=300,damage=3)
        self.name = "Twin Strike"
        self.bulletSpacing = 20
        
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        bulletList = []
        playerPosX -= self.bulletSpacing//2

        for i in range(self.bulletAmt):
            bulletList.append(Bullet(playerPosX + (i * self.bulletSpacing),playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite))
            
        return bulletList
        
class TripleShot(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,5,fireRate=400,damage=2)
        self.name = "Fusillade"
        
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        bulletList = []
        velocityX = -2
        if self.isEnemyGear:
            velocityY = 10
        else:
            velocityY = -10

        for i in range(self.bulletAmt):
            self.velocity = [velocityX,velocityY]
            bulletList.append(Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite))
            velocityX += 1
            
        return bulletList
    
class MachineGun(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,2,fireRate = 125,damage=1)
        self.name = "Machine Gun"
        
    def getBulletList(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
        bulletList = []
        velocityY = -10
        
        if self.isEnemyGear:
            velocityY = 10

        for i in range(self.bulletAmt):
            velocityX = rnd.uniform(-2,2)
            self.velocity = [velocityX,velocityY]
            bulletList.append(Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite,self.pierce))

        return bulletList
    
class Sniper(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,1,7,900,7,2,25)
        self.name = "Sniper"
        self.bulletSprite = ("sprites\SniperRound.png",14,14)
        
    def getBulletList(self,playerPosX:float,playerPosY:float,playerRad:float) -> list:
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite,self.pierce)]
    
class BlackHole(Gear):
    def __init__(self,isForEnemy: bool = False) -> None:
        super().__init__(isForEnemy,1,15,1500,10,10,3)
        self.name = "Black Hole"
        
    def getBulletList(self,playerPosX:float,playerPosY:float,playerRad:float) -> list:
        return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite,self.pierce)]
        



