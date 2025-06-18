from bullet import *
import random as rnd

def singleShot(self, playerPosX:float,playerPosY:float,playerRad:float):
    return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite)]
    
def doubleShot(self, playerPosX:float,playerPosY:float,playerRad:float):
    bulletList = []
    playerPosX -= 10

    for i in range(self.bulletAmt):
        bulletList.append(Bullet(playerPosX + (i * 20),playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite))
            
    return bulletList

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

def sniper(self,playerPosX:float,playerPosY:float,playerRad:float) -> list:
    return [Bullet(playerPosX,playerPosY - playerRad,self.radius,self.velocity,self.bulletSprite,self.pierce)]
    