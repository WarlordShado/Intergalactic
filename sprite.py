import pygame

class Sprite():
    def __init__(self,imagePath:str,width:float,height:float) -> None:
        self.image = pygame.image.load(imagePath).convert_alpha()
        self.imageSurface = pygame.Surface([width, height], pygame.SRCALPHA)
        self.imageSurface.blit(self.image,(0,0))

    def getImage(self, screen: pygame.Surface,position:tuple) -> None:
        screen.blit(self.imageSurface,position)

    def updateAnimation(self): #Not Used, for now
        pass