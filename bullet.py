import pygame
from sprite import *
import math

class Bullet():
    def __init__(self,xpos:float,ypos:float,rad:int,velocity:list,pierce:int = 0,isSniper:bool = False):
        self.pos = pygame.Vector2([xpos,ypos])
        self.rad = rad
        self.velocity = velocity
        self.pierce = pierce
        self.bulletColor = (0,0,0)

        if isSniper:
            self.bulletImage = Sprite("sprites\SniperRound.png",14,14)
        else:
            if self.velocity[1] > 1:
                self.bulletImage = Sprite("sprites\EnemyBullet.png",10,10)
            else:
                self.bulletImage = Sprite("sprites\BasicBullet.png",10,10)
        
    def moveBullet(self) -> None:
        self.pos.x += self.velocity[0]
        self.pos.y += self.velocity[1]
        
    def drawBullet(self,screen:pygame.Surface) -> None:
        pygame.draw.circle(screen,self.bulletColor,(self.pos.x,self.pos.y),self.rad,0)
        self.bulletImage.getImage(screen,(self.pos.x - self.rad,self.pos.y - self.rad))
        
    def update(self) -> None:
        pass
    
    def getRad(self) -> float:
        return self.rad

    def getX(self) -> float:
        return self.pos.x

    def getY(self) -> float:
        return self.pos.y

class KillBullet(Bullet):
    def __init__(self,xpos:float,ypos:float,rad:int,velocity:list) -> None:
        super().__init__(xpos,ypos,rad,velocity)
        self.bulletColor = (255,0,0)
        
    def drawBullet(self,screen:pygame.Surface) -> None:
        pygame.draw.circle(screen,self.bulletColor,(self.pos.x,self.pos.y),self.rad,0)
    
class HomingBullet(Bullet):
    def __init__(self,xpos:float,ypos:float,rad:int,velocity:list,lockedEnemy,agg: int = 11) -> None:
        super().__init__(xpos,ypos,rad,velocity)
        self.lockedEnemy = lockedEnemy
        self.aggresiveness = agg
        self.bulletImage = Sprite("sprites\HomingMissle.png",20,20)
        
    def drawBullet(self,screen:pygame.Surface) -> None:
        pygame.draw.circle(screen,self.bulletColor,(self.pos.x,self.pos.y),self.rad,0)
        self.bulletImage.getImage(screen,(self.pos.x - self.rad,self.pos.y - self.rad))
        
    def update(self) -> None:
        enemyPos = pygame.Vector2([self.lockedEnemy.getX(),self.lockedEnemy.getY()])
        direction = enemyPos - self.pos

        if len(direction) != 0:
            self.velocity = direction.normalize() * self.aggresiveness
        self.pos += self.velocity
        
