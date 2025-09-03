import pygame
from sprite import Sprite

class Bullet():
    def __init__(self,xpos:float,ypos:float,rad:int,velocity:list,bullet_sprite:tuple,pierce:int = 0):
        self.pos : pygame.Vector2 = pygame.Vector2([xpos,ypos])
        self.rad : int = rad
        self.velocity : list = velocity
        self.pierce : int = pierce
        self.bulletColor : tuple = (0,0,0)
        self.bulletImage = Sprite(bullet_sprite[0],bullet_sprite[1],bullet_sprite[2])
                
        if rad > 10: #Only used if bullet doesnt already have a sprite
            self.bulletColor = (255,0,0)
        
    def moveBullet(self) -> None:
        self.pos.x += self.velocity[0]
        self.pos.y += self.velocity[1]
        
    def drawBullet(self,screen:pygame.Surface) -> None:
        pygame.draw.circle(screen,self.bulletColor,(self.pos.x,self.pos.y),self.rad,0)
        if self.bulletImage != 0:
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
    def __init__(self,xpos:float,ypos:float,bulletSprite:tuple,rad:int = 15,velocity:list = []) -> None:
        super().__init__(xpos,ypos,rad,velocity,bulletSprite)
        self.bulletColor : tuple = (0,0,0)
        
