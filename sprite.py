import pygame

class Sprite():
    def __init__(self,imagePath:str,width:float,height:float) -> None:
        self.width = width
        self.height = height
        self.frames = []
        self.framerateTimer = 0
        self.currentFrame = 0
        self.image = pygame.image.load(imagePath).convert_alpha()
        imageWidth = self.image.get_width()
        
        for i in range(imageWidth//int(self.width)):
            frame_rect = pygame.Rect(i * self.width,0,self.width,self.height)
            self.frames.append(self.image.subsurface(frame_rect))
        self.frameAmt = len(self.frames) - 1
        self.imageSurface = pygame.Surface([width, height], pygame.SRCALPHA)
        self.imageSurface.blit(self.frames[0],(0,0))

    def getImage(self, screen: pygame.Surface,position:tuple) -> None:
        screen.blit(self.imageSurface,position)
        self.updateAnimation()

    def updateAnimation(self): #Not Used, for now
        self.framerateTimer += 1
        if self.framerateTimer >= 6:
            self.framerateTimer = 0
            self.imageSurface.blit(self.frames[self.currentFrame],(0,0))
            self.currentFrame += 1
            if self.currentFrame >= len(self.frames) - 1:
                self.currentFrame = 0
                