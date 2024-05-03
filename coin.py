import pygame

class Coin:
    def __init__(self,value: int,color: (),startX: float,startY:float,rad:int):
        self.val = value
        self.color = color
        self.x = startX
        self.y = startY
        self.rad = rad
        
    def drawCoin(self,screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.rad,0)
        
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
    def __init__(self,value: int,color: (),startX:float,startY:float,rad:int):
        super().__init__(value,color,startX,startY,rad)
        
    def drawCoin(self,screen:pygame.Surface) -> None:
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.rad,0)
        