import pygame
from sprite import Sprite
from bullet import Bullet, KillBullet
from gear import Gear, TripleShot, MachineGun, DoubleShot
from random import randint as rnd

ROUND_MOD = 5

class Enemy():
    def __init__(self,xPos:float,yPos:float,rad:int,hasCoin:bool,round:int = 1) -> None:
        self.x = xPos
        self.y = yPos
        self.rad = rad
        self.speed = 5
        self.hasCoin = hasCoin
        self.gear = Gear(True)
        self.fireRate = 500
        self.enemySprite = Sprite("sprites\Enemy.png",30,30)
        self.healthFunc = lambda health,round: health if round <= ROUND_MOD else health + int(round / ROUND_MOD)
        self.health = self.healthFunc(1,round)
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
    def __init__(self,xPos:float,yPos:float,rad:int,hasCoin:bool,round:int = 1) -> None:
        super().__init__(xPos,yPos,rad,hasCoin)
        self.enemySprite = Sprite("sprites\StrongEnemy.png",30,30)
        self.healthFunc = lambda health: health if round <= ROUND_MOD else health + (int(round / ROUND_MOD) * 1.5)
        self.health = self.healthFunc(3)
        self.scoreVal = 300
    
class Boss(Enemy): #Used as a Structure for inheritance
    def __init__(self,xPos:float,yPos:float,rad:int,round:int = 1) -> None:
        super().__init__(xPos,yPos,rad,True,round)
        self.healthFunc = lambda health,round: health if round <= ROUND_MOD else health + (int(round / ROUND_MOD) * 2)
        self.maxHp = self.healthFunc(1,round)
        self.health = self.healthFunc(1,round)
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
    
    def getName(self) -> str:
        return self.name
            
class Goliath(Boss):
    def __init__(self,xPos:float,yPos:float,rad:int,round:int = 1) -> None:
        super().__init__(xPos,yPos,rad)
        self.maxHp = self.healthFunc(50,round)
        self.health = self.healthFunc(45,round)
        self.color = (255,0,0)
        self.name = "Goliath"
        self.gear =  DoubleShot(True) 
        self.fireRate = 40
        self.specRate = 250
        self.enemySprite = Sprite("sprites\Goliath.png",60,60)
        
    def special(self) -> None:
        if self.health < self.maxHp:
            self.health += 3

class Teleporter(Boss): #I hate this thing. Fix it. Teleport is breaking it. IDK why
    def __init__(self,xPos:float,yPos:float,rad:int,scrWidth:int,round:int = 1) -> None:
        super().__init__(xPos,yPos,rad,round)
        self.scrWidth = scrWidth
        self.maxHp = self.healthFunc(25,round)
        self.health = self.healthFunc(25,round)
        self.color = (255,0,0)
        self.name = "Telefrag"
        self.gear = MachineGun(True)
        self.fireRate = 40
        self.specRate = 75
        self.enemySprite = Sprite("sprites\Telefrag.png",60,60)
        
    def special(self) -> None:
        getLoc = rnd(int(self.rad*2),int(self.scrWidth - (self.rad*2)))
        self.x = getLoc

class Overseer(Boss):
    def __init__(self,xPos:float,yPos:float,rad:int,round:int = 1) -> None:
        super().__init__(xPos,yPos,rad,round)
        self.maxHp = self.healthFunc(20,round)
        self.health = self.healthFunc(20,round)
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
    def __init__(self, xPos: float, yPos: float, rad: int,round:int = 1) -> None:
        super().__init__(xPos, yPos, rad,round)
        self.maxHp = self.healthFunc(15,round)
        self.health = self.healthFunc(15,round)
        self.color = (0,255,255)
        self.name = "Rouge"
        self.gear = TripleShot(True)
        self.fireRate = 30
        self.specRate = 100
        self.enemySprite = Sprite("sprites\Rouge.png",60,60)
        
    def special(self, screen:pygame.Surface) -> list:
        return [KillBullet(self.getX(),self.getY() + self.rad,velocity=[0,7.5],bulletSprite=("sprites\KillBullet.png",30,30))]
    
class Minion(Boss):
    def __init__(self,xPos: float,yPos: float,rad: int) -> None:
        super().__init__(xPos,yPos,rad)
        self.health = 3
        self.fireRate = 250
        self.enemySprite = Sprite("sprites\Minion.png",30,30)