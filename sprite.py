import pygame

class Sprite():
    def __init__(self,imagePath:str,width:float,height:float) -> None:
        self.width:float = width
        self.height:float = height
        self.frames:list = []
        self.column = 0
        self.framerateTimer:int = 0
        self.currentFrame:int = 0
        self.image:pygame.Surface = pygame.image.load(imagePath).convert_alpha()
        imageWidth:int = self.image.get_width()
        
        for i in range(0,imageWidth//int(self.width),1):
            frame_rect:pygame.Rect = pygame.Rect(i * self.width,0,self.width,self.height)
            self.frames.append(self.image.subsurface(frame_rect))
            
        self.frameAmt:int = len(self.frames) - 1
        self.imageSurface:pygame.Surface = pygame.Surface([width, height], pygame.SRCALPHA)
        self.imageSurface.blit(self.frames[0],(0,0))

    def getImage(self, screen: pygame.Surface,position:tuple) -> None:
        screen.blit(self.imageSurface,position)
        self.updateAnimation()

    def updateAnimation(self) -> None:
        self.framerateTimer += 1
        if self.framerateTimer >= 6: #6 comes out to about 10 animation frames a second for all
            self.framerateTimer = 0
            self.imageSurface.blit(self.frames[self.currentFrame],(0,0))
            self.currentFrame += 1
            if self.currentFrame > len(self.frames) - 1:
                self.currentFrame = 0 
                
    def changeAnimation(self,column:int):
        self.column = column
                
#Turn Frames into 2d array
#Increase column by one when the class calls to
#set extra timer to run so the class knows when to go back to the original sprite
            
            
                