import pygame

class Bullet():
    def __init__(self,xpos:float,ypos:float,rad:int,velocity:int):
        self.x = xpos
        self.y = ypos
        self.rad = rad
        self.velocity = velocity
        self.bulletColor = (0,255,0)
        
    def moveBullet(self) -> None:
        self.y -= self.velocity
        
    def drawBullet(self,screen:pygame.Surface) -> None:
        if self.velocity < 1:
            self.bulletColor = (255,0,129)

        pygame.draw.circle(screen,self.bulletColor,(self.x,self.y),self.rad,0)
    
    def getRad(self) -> float:
        return self.rad

    def getX(self) -> float:
        return self.x

    def getY(self) -> float:
        return self.y