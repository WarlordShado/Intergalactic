from enemy import *
from gameData.enemyData import *
from gameData.bossData import *

def squareFormFunc(self,center): #SquareFormation
        Count:int = 0
        startX:int = (center - (self.enemySpacing * 2))
        startY:int = self.enemySpacing + 25

        for i in range(25):
            self.enemyList.append(Enemy(startX,startY,15,ENEMY_DATA_ARRAY["Basic_Enemy"],self.round))
            #print("(" , startX , "," , startY , ")")
            startX += self.enemySpacing
            if Count >= 4:
                startY += self.enemySpacing
                Count = 0
                startX = center - (self.enemySpacing * 2)
            else:
                Count += 1

def diamondFormFunc(self,center): #DiamondFormation
    startX:int = center
    startY:int = ((self.enemySpacing * 2) + 135)
        
    for i in range(4): #Makes the Inner Diamond
        self.enemyList.append(Enemy(startX,startY,15,ENEMY_DATA_ARRAY["Strong_Enemy"],self.round))
            
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
        self.enemyList.append(Enemy(startX,startY,15,ENEMY_DATA_ARRAY["Basic_Enemy"]))
            
        if i < 2 or i == 6:
            startX -= self.enemySpacing
        else:
            startX += self.enemySpacing
                
        if i < 4:
            startY -= self.enemySpacing
        else:
            startY += self.enemySpacing

def goliathFormFunc(self,center):
    startX:int = center
    startY:int = 120
    self.enemyList.append(Boss(startX,startY,30,BOSS_DATA_ARRAY['Goliath']))

def rougeFormFunc(self,center):
    startX:int = center
    startY:int = 120
    self.enemyList.append(Boss(startX,startY,30,BOSS_DATA_ARRAY['Rouge']))

def hiveFormFunc(self,center):
    startX:int = center
    startY:int = 120
    self.enemyList.append(Boss(startX,startY,30,BOSS_DATA_ARRAY['Overseer']))

    startX = (center - self.enemySpacing)
    startY = self.enemySpacing
        
    for i in range(9):
        self.enemyList.append(Enemy(startX,startY,15,ENEMY_DATA_ARRAY["Overseer_Minion"],self.round))
        startX += 30
        if i < 4:
            startY += 30
        else:
            startY -= 30