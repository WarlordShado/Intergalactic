import pygame
from pygame.surface import Surface
from enemy import *
from bullet import Bullet
from random import randint

class Formation(): #Template
    def __init__(self,screenWidth:float,screenHeight:float,round:int = 1) -> None:
        self.screenWidth:float = screenWidth
        self.screenHeight:float = screenHeight
        self.round:int = round
        self.enemyList:list = []
        
    def getRandEnemy(self) -> Enemy:
        return self.enemyList[rnd.randint(0,len(self.enemyList) - 1)]
    
    def createFormation(self) -> None:
        pass
    
    def drawEnemies(self,win:pygame.Surface) -> None:
        for enemy in self.enemyList:
            enemy.drawEnemy(win)
    
    def enemyShoot(self) -> Bullet:
        bulletList:list = []
        
        for enemy in self.enemyList:
            rndShoot = randint(0,enemy.fireRate)
            if rndShoot == 10:
                bulletCheck = enemy.shoot()
                for item in bulletCheck:
                    bulletList.append(item)
                
        return bulletList
        
    def update(self) -> None:
        reverseEnemy:bool = False
        for enemy in self.enemyList: #Checks if enemies need to start going the other way
            if enemy.getX() - enemy.rad <= 0 or enemy.getX() + enemy.rad >= self.screenWidth:
                reverseEnemy = True
                break
            
        for enemy in self.enemyList: #Moves the Enemies
            if reverseEnemy: #Reverses the enemy speed if needed
                enemy.reverseSpeed()
            enemy.moveEnemy()
    
class BossFormation(Formation):
    def __init__(self,screenWidth:float,screenHeight:float,BossType: Boss,round:int = 1) -> None:
        super().__init__(screenWidth,screenHeight,round)
        self.Boss:Boss = BossType
        
    def drawEnemies(self, win: Surface) -> None:
        self.Boss.drawEnemy(win)
        
    def enemyShoot(self) -> Bullet:
        bulletList:list = []

        rndShoot = randint(0,self.Boss.fireRate)
        if rndShoot == 5:
             bulletCheck = self.Boss.shoot()
             for item in bulletCheck:
                 bulletList.append(item)
                 
        return bulletList
    
    def useSpecial(self, win: pygame.Surface) -> Bullet:
        bulletAdd:list = []

        rndSpec:int = randint(0,self.Boss.specRate)
        if rndSpec == self.Boss.specRate // 2:
             if type(self.Boss) is Rouge:
                 
                 bulletCheck = self.Boss.special(win)
                 
                 for item in bulletCheck:
                     bulletAdd.append(item)
             else:
                 self.Boss.special()
                 
        return bulletAdd
        
    def update(self) -> None:
        self.Boss.moveEnemy()
            
        if not (self.Boss.getX() + self.Boss.getRad() < self.screenWidth and self.Boss.getX() - self.Boss.getRad() > 0):
            self.Boss.reverseSpeed()
            
class HiveFormation(BossFormation):
    def __init__(self,screenWidth:float,screenHeight:float,BossType: Overseer,round:int = 1) -> None:
        super().__init__(screenWidth,screenHeight,BossType,round)
        self.enemySpacing:int = 120
        
    def drawEnemies(self, win: Surface) -> None:
        self.Boss.drawEnemy(win)
        
        for item in self.Boss.minionList:
             item.drawEnemy(win)
             
    def createFormation(self,center) -> None:
        startX:int = (center - self.enemySpacing)
        startY:int = self.enemySpacing
        
        for i in range(9):
            self.Boss.minionList.append(Minion(startX,startY,15))
            startX += 30
            if i < 4:
                startY += 30
            else:
                startY -= 30
                
    def enemyShoot(self) -> Bullet:
        bulletList:list = []
        if len(self.Boss.minionList) > 0:
            for enemy in self.Boss.minionList:
                rndShoot = randint(0,enemy.fireRate)
                if rndShoot == 10:
                    bulletCheck = enemy.shoot()
                    for item in bulletCheck:
                        bulletList.append(item)
        else:
            rndShoot = randint(0,self.Boss.fireRate)
            if rndShoot == 10:
                bulletList = self.Boss.shoot()
                
        return bulletList

    def update(self) -> None:
        reverseEnemy:bool = False
        
        if self.Boss.getX() - self.Boss.rad <= 0 or self.Boss.getX() + self.Boss.rad >= self.screenWidth:
            reverseEnemy = True

        if not reverseEnemy:
            for enemy in self.Boss.minionList: #Checks if enemies need to start going the other way
                if enemy.getX() - enemy.rad <= 0 or enemy.getX() + enemy.rad >= self.screenWidth:
                    reverseEnemy = True
                    break
            
        for enemy in self.Boss.minionList: #Moves the Minions
            if reverseEnemy: #Reverses the enemy speed if needed
                enemy.reverseSpeed()
            enemy.moveEnemy()
            
        if reverseEnemy:
            self.Boss.reverseSpeed()
        self.Boss.moveEnemy()

class SquareForm(Formation):
    def __init__(self,screenWidth:float,screenHeight:float,round:int = 1) -> None:
        super().__init__(screenWidth,screenHeight,round)
        self.enemySpacing = 50
        
    def createFormation(self,center) -> None:
        Count:int = 0
        startX:int = (center - (self.enemySpacing * 2))
        startY:int = self.enemySpacing + 25

        for i in range(25):
            hasCoin:bool = False
            checkCoin:int = randint(0,15)
            
            if checkCoin == 1:
                hasCoin = True
            
            self.enemyList.append(Enemy(startX,startY,15,hasCoin,self.round))
            #print("(" , startX , "," , startY , ")")
            startX += self.enemySpacing
            if Count >= 4:
                startY += self.enemySpacing
                Count = 0
                startX = center - (self.enemySpacing * 2)
            else:
                Count += 1
                
class DiamondForm(Formation):
    def __init__(self,screenWidth:float,screenHeight:float,round:int = 1) -> None:
        super().__init__(screenWidth,screenHeight,round)
        self.enemySpacing = 35
        
    def createFormation(self,center) -> None:
        startX:int = center
        startY:int = ((self.enemySpacing * 2) + 135)
        
        for i in range(4): #Makes the Inner Diamond
            hasCoin = False
            checkCoin = randint(0,15)
            
            if checkCoin == 1:
                hasCoin = True

            self.enemyList.append(StrongEnemy(startX,startY,15,hasCoin,self.round))
            
            if i <= 0:
                startX += self.enemySpacing
            else:
                startX -= self.enemySpacing
                
            if i < 2:
                startY -= self.enemySpacing
            else:
                startY += self.enemySpacing
                
        startX = center
        startY = ((self.enemySpacing * 2) + 170)
        
        for i in range(8):
            hasCoin = False
            checkCoin = randint(0,15)
            
            if checkCoin == 1:
                hasCoin = True

            self.enemyList.append(Enemy(startX,startY,15,hasCoin))
            
            if i < 2 or i == 6:
                startX -= self.enemySpacing
            else:
                startX += self.enemySpacing
                
            if i < 4:
                startY -= self.enemySpacing
            else:
                startY += self.enemySpacing