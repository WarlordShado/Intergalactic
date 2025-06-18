import pygame
from sprite import Sprite

class Coin:
    def __init__(self,value: int,startX: float,startY:float,rad:int) -> None:
        self.val : int = value
        self.color : tuple = (0,0,0)
        self.x : float = startX
        self.y : float  = startY
        self.rad : int = rad
        self.coinSprite : Sprite = Sprite("sprites/Coin.png",10,10)
        
    def drawCoin(self,screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.rad,0)
        self.coinSprite.getImage(screen,(self.x - self.rad,self.y - self.rad))
        
    def getVal(self) -> int:
        return self.val

    def moveCoin(self) -> None:
        self.y += 5
        
    def getRad(self) -> float:
        return self.rad
        
    def getX(self) -> float:
        return self.x
    
    def getY(self) -> float:
        return self.y
    
class BossToken(Coin):
    def __init__(self,value: int,startX:float,startY:float,rad:int) -> None:
        super().__init__(value,startX,startY,rad)
        self.coinSprite : Sprite = Sprite("sprites/BossToken.png",30,30)
        