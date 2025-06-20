import pygame
from pygame.surface import Surface
from enemy import *
from bullet import Bullet
from random import randint
from gameData.enemyData import ENEMY_DATA_ARRAY
from gameData.formationData import *
from gameData.formationFuncs import *
from Globals import *

class Formation(): #Template
    def __init__(self,screenWidth:float,screenHeight:float,formationData:dict,round:int = 1) -> None:
        self.screenWidth:float = screenWidth
        self.screenHeight:float = screenHeight
        self.round:int = round
        self.enemyList:list = []
        self.formFunc = formationData['funcName']
        self.enemySpacing = formationData['spacing']
        
    def getRandEnemy(self) -> Enemy:
        return self.enemyList[rnd.randint(0,len(self.enemyList) - 1)]
    
    def createFormation(self,center) -> None:
        self.formFunc(self,center)
    
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
            if type(enemy) is Boss:
                rndSpec = randint(0,enemy.specRate)
                if rndSpec == 10:
                    bulletCheck = enemy.special()
                    if type(bulletCheck) is not None:
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

    def hasBoss(self)->bool:
        for enemy in self.enemyList:
            if type(enemy) is Boss:
                return True
        return False
    
    def getBossHealth(self)->tuple:
        if not self.hasBoss(): return (0,0)
        for enemy in self.enemyList:
            if type(enemy) is Boss: return (enemy.maxHp,enemy.health)
        return (0,0)
    
    def getBossName(self)->str:
        if not self.hasBoss(): return ""
        for enemy in self.enemyList:
            if type(enemy) is Boss: return enemy.name
        return ""