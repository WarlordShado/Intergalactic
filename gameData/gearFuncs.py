from bullet import *
import random as rnd

def singleShot(self, playerPosX:float,playerPosY:float,playerRad:float):
    return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite)]
    
def singleShotLvl(self,lvl):
    self.dmg += 1
    if lvl % 3 == 0: self.fireRate -= 10 if self.fireRate >= 100 else 0
    if lvl % 5 == 0: self.pierce += 1 if self.pierce <= 3 else 0

def doubleShot(self, playerPosX:float,playerPosY:float,playerRad:float):
    bulletList = []
    playerPosX -= 10

    for i in range(self.bulletAmt):
        bulletList.append(Bullet(playerPosX + (i * 20),playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite))
            
    return bulletList

def doubleShotLvl(self,lvl):
    if lvl % 2 == 0: self.dmg += 1
    if lvl % 4 == 0: self.fireRate -= 15 if self.fireRate >= 150 else 0

def tripleShot(self, playerPosX:float,playerPosY:float,playerRad:float):
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

def tripleShotLvl(self,lvl):
    if lvl % 3 == 0:self.dmg += 1
    if lvl % 5 == 0:self.fireRate -= 10 if self.fireRate >= 250 else 0

def machineGun(self, playerPosX:float,playerPosY:float,playerRad:float) -> list:
    bulletList = []
    velocityY = -10
        
    if self.isEnemyGear:
        velocityY = 10

    for i in range(self.bulletAmt):
        velocityX = rnd.uniform(-2,2)
        self.velocity = [velocityX,velocityY]
        bulletList.append(Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite,self.pierce))

    return bulletList

def machineGunLvl(self,lvl):
    if lvl % 3 == 0:self.dmg += 1
    if lvl % 5 == 0:self.fireRate -= 5 if self.fireRate >= 75 else 0

def sniper(self,playerPosX:float,playerPosY:float,playerRad:float) -> list:
    return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite,self.pierce)]
    
def sniperLvl(self,lvl):
    if lvl % 3 == 0:
        self.dmg += 3
        self.pierce += 1 if self.pierce >= 5 else 0
    