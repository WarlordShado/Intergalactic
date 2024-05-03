import pygame

class Coin:
    def __init__(self,value,color,startX,startY,rad):
        self.val = value
        self.color = color
        self.x = startX
        self.y = startY
        self.rad = rad
        
    def drawCoin(self,screen) -> None:
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
    def __init__(self,value,color,startX,startY,rad):
        super().__init__(value,color,startX,startY,rad)
        
    def drawCoin(self,screen) -> None:
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.rad,0)
        