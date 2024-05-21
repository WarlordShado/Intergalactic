import pygame
from sprite import *
from bullet import *
from gear import *

class Enemy():
    def __init__(self,xPos:float,yPos:float,rad:int,hasCoin:bool) -> None:
        self.x = xPos
        self.y = yPos
        self.rad = rad
        self.speed = 5
        self.hasCoin = hasCoin
        self.gear = Gear(True)
        self.fireRate = 500
        self.enemySprite = Sprite("sprites\Enemy.png",30,30)
        self.health = 1
        self.scoreVal = 100
        
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
    
class StrongEnemy(Enemy):
    def __init__(self,xPos:float,yPos:float,rad:int,hasCoin:bool) -> None:
        super().__init__(xPos,yPos,rad,hasCoin)
        self.enemySprite = Sprite("sprites\StrongEnemy.png",30,30)
        self.health = 3
        self.scoreVal = 300
    
class Boss(Enemy): #Used as a Structure for inheritance
    def __init__(self,xPos:float,yPos:float,rad:int) -> None:
        super().__init__(xPos,yPos,rad,True)
        self.maxHp = 1
        self.health = 1
        self.color = (0,0,0)
        self.name = ""
        self.fireRate = 20
        self.specRate = 500
        
    def canBeHurt(self) -> bool:
        return True
        
    def startSpecial(self,screen: pygame.Surface) -> None:
        pass 
    
    def special(self) -> None:
        return None
    
    def getName(self):
        return self.name
            
class Goliath(Boss):
    def __init__(self,xPos:float,yPos:float,rad:int) -> None:
        super().__init__(xPos,yPos,rad)
        self.maxHp = 50
        self.health = 45
        self.color = (255,0,0)
        self.name = "Goliath"
        self.gear =  DoubleShot(True) 
        self.fireRate = 40
        self.specRate = 250
        self.enemySprite = Sprite("sprites\Goliath.png",60,60)
        
    def special(self) -> None:
        if self.health < self.maxHp:
            self.health += 3

class Teleporter(Boss):
    def __init__(self,xPos:float,yPos:float,rad:int,scrWidth:int) -> None:
        super().__init__(xPos,yPos,rad)
        self.scrWidth = scrWidth
        self.maxHp = 25
        self.health = 25
        self.color = (255,0,0)
        self.name = "Telefrag"
        self.gear = MachineGun(True)
        self.fireRate = 40
        self.specRate = 75
        self.enemySprite = Sprite("sprites\Telefrag.png",60,60)
        
    def special(self) -> None:
        getLoc = rnd.randint(int(self.rad),int(self.scrWidth - self.rad))
        self.x = getLoc

class Overseer(Boss):
    def __init__(self,xPos:float,yPos:float,rad:int) -> None:
        super().__init__(xPos,yPos,rad)
        self.maxHp = 20
        self.health = 20
        self.color = (0,255,255)
        self.name = "Hive Mind"
        self.minionList = []
        self.gear = Gear(True)
        self.fireRate = 50
        self.enemySprite = Sprite("sprites\Hive.png",60,60)
            
    def canBeHurt(self) -> bool:
        if len(self.minionList) == 0:
            return True
        return False
    
class Rouge(Boss):
    def __init__(self, xPos: float, yPos: float, rad: int) -> None:
        super().__init__(xPos, yPos, rad)
        self.maxHp = 15
        self.health = 15
        self.color = (0,255,255)
        self.name = "Rouge"
        self.gear = TripleShot(True)
        self.fireRate = 30
        self.specRate = 100
        self.enemySprite = Sprite("sprites\Rouge.png",60,60)
        
    def special(self, screen:pygame.Surface) -> list:
        return [KillBullet(self.getX(),self.getY() + self.rad,25,[0,7.5])]
            
    
class Minion(Boss): #Boss Minion, They can't move
    def __init__(self,xPos: float,yPos: float,rad: int) -> None:
        super().__init__(xPos,yPos,rad)
        self.health = 3
        self.fireRate = 250
        self.enemySprite = Sprite("sprites\Minion.png",30,30)