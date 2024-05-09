import pygame
import math

class Bullet():
    def __init__(self,xpos:float,ypos:float,rad:int,velocity:list,pierce:int = 0):
        self.pos = pygame.Vector2([xpos,ypos])
        self.rad = rad
        self.velocity = velocity
        self.pierce = pierce
        self.bulletColor = (0,255,0)
        
    def moveBullet(self) -> None:
        self.pos.x += self.velocity[0]
        self.pos.y += self.velocity[1]
        
    def drawBullet(self,screen:pygame.Surface) -> None:
        if self.velocity[1] > 1:
            self.bulletColor = (255,0,129)

        pygame.draw.circle(screen,self.bulletColor,(self.pos.x,self.pos.y),self.rad,0)
        
    def update(self) -> None:
        pass
    
    def getRad(self) -> float:
        return self.rad

    def getX(self) -> float:
        return self.pos.x

    def getY(self) -> float:
        return self.pos.y

class KillBullet(Bullet):
    def __init__(self,xpos:float,ypos:float,rad:int,velocity:list):
        super().__init__(xpos,ypos,rad,velocity)
        self.bulletColor = (255,0,0)
        
    def drawBullet(self,screen:pygame.Surface) -> None:
        pygame.draw.circle(screen,self.bulletColor,(self.pos.x,self.pos.y),self.rad,0)
    
class HomingBullet(Bullet):
    def __init__(self,xpos:float,ypos:float,rad:int,velocity:list,lockedEnemy) -> None:
        super().__init__(xpos,ypos,rad,velocity)
        self.lockedEnemy = lockedEnemy
        self.bulletColor = (0,255,255)
        
    def drawBullet(self,screen:pygame.Surface) -> None:
        pygame.draw.circle(screen,self.bulletColor,(self.pos.x,self.pos.y),self.rad,0)
        
    def update(self) -> None:
        enemyPos = pygame.Vector2([self.lockedEnemy.getX(),self.lockedEnemy.getY()])
        direction = enemyPos - self.pos
        if len(direction) != 0:
            self.velocity = direction.normalize() * 11
        self.pos += self.velocity
        
