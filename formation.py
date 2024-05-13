import pygame
from enemy import *
import random as rnd

class Formation(): #Template
    def __init__(self,screenWidth:float,screenHeight:float) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.enemyList = []
        
    def getRandEnemy(self) -> Enemy:
        return self.enemyList[rnd.randint(0,len(self.enemyList) - 1)]
        
    def createFormation(self) -> None:
        pass
    
    def drawEnemies(self,win:pygame.Surface) -> None:
        pass
    
    def update(self):
        pass

class SquareForm(Formation):
    def __init__(self,screenWidth:float,screenHeight:float) -> None:
        super().__init__(screenWidth,screenHeight)
        self.enemySpacing = 50
        
    def createFormation(self,center) -> None:
        Count = 0
        startX = (center - (self.enemySpacing * 2))
        startY = self.enemySpacing + 25

        for i in range(25):
            hasCoin = False
            checkCoin = rnd.randint(0,15)
            
            if checkCoin == 1:
                hasCoin = True
            
            self.enemyList.append(Enemy(startX,startY,15,hasCoin))
            #print("(" , startX , "," , startY , ")")
            startX += self.enemySpacing
            if Count >= 4:
                startY += self.enemySpacing
                Count = 0
                startX = center - (self.enemySpacing * 2)
            else:
                Count += 1
                
    def drawEnemies(self,win:pygame.Surface) -> None:
        for enemy in self.enemyList:
            enemy.drawEnemy(win)
            
    def update(self):
        reverseEnemy = False
        for enemy in self.enemyList: #Checks if enemies need to start going the other way
            if enemy.getX() - enemy.rad <= 0 or enemy.getX() + enemy.rad >= self.screenWidth:
                reverseEnemy = True
                break
            
        for enemy in self.enemyList: #Moves the Enemies
            if reverseEnemy: #Reverses the enemy speed if needed
                enemy.reverseSpeed()
            enemy.moveEnemy()
