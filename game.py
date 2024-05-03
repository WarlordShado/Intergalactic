import enum
import math
import pygame
import pygame.freetype
import random
from coin import *
from player import *
from bullet import *
from enemy import *

class Game():
    def __init__(self,screen,center,height):
        self.SCREENCENTER = center
        self.win = screen
        self.player = Player(center,height - 75,25)
        self.height = height
        self.center = center
        self.bullets = []
        self.enemies = []
        self.enemiesBullets = []
        self.coins = []
        self.shootState = True
        self.score = 0
        self.makeEnemies()
        self.gameOver = False
        self.startGame = False
        self.round = 1
        
        self.isBossRound = False
        self.Boss = None

    def renderLables(self) -> None:
        font = pygame.freetype.SysFont("Comic Sans MS",32)
        font.render_to(self.win,(5,5),"Score: " + str(self.score),(255,255,255))
        
        font = pygame.freetype.SysFont("Comic Sans MS",32)
        font.render_to(self.win,(350,5),"Multiplyer: X" + str(self.player.getScoreMultiplyer()),(255,255,255))
        
        if self.isBossRound:
            font = pygame.freetype.SysFont("Comic Sans MS",32)
            font.render_to(self.win,(150,47),"Boss Health: " + str(self.Boss.health) + "/30",(255,0,0))
        
    def addScore(self,scoreAmt) -> None:
        self.score += scoreAmt * self.player.getScoreMultiplyer()

    def handleInput(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.movePlayer(-5)
               
        if keys[pygame.K_RIGHT]:
            self.player.movePlayer(5)
            
        if keys[pygame.K_UP] and self.shootState: 
            bulletAdd = self.player.shoot()
            self.bullets.append(bulletAdd)
            self.shootState = False

    def changeShootState(self,state) -> None:
        self.shootState = state
        
    def makeEnemies(self) -> None:
        ENEMYSPACING = 100
        startX = self.SCREENCENTER - ENEMYSPACING * 2
        startY = ENEMYSPACING
        
        for i in range(1,16):
            rnd = random.randint(1,15)
            if rnd == 10:
                self.enemies.append(Enemy(startX,startY,15,True))
            else:
                self.enemies.append(Enemy(startX,startY,15,False))
            startX += ENEMYSPACING
                
            if i % 5 == 0:
                startX = self.SCREENCENTER - ENEMYSPACING * 2
                startY += ENEMYSPACING
                
    def makeBoss(self) -> None:
        startX = self.SCREENCENTER
        startY = 125
        self.Boss = Boss(startX,startY,30)
        self.Boss.makeMinions(self.win)
                
    def moveEnemies(self) -> None:
        if not self.isBossRound:
            for enemy in (self.enemies):
                enemy.moveEnemy()
                rnd = random.randint(1,10)
                if rnd == 5 :
                    enemy.reverseSpeed()
        else:
            self.Boss.moveEnemy()
            rnd = random.randint(1,10)
            if rnd == 5 :
                self.Boss.reverseSpeed()
         
                
    def enemyShoot(self) -> None:
        if not self.isBossRound:
            for enemy in (self.enemies):
                rnd = random.randint(0,200)
                if rnd == 10:
                    bulletAdd = enemy.shoot()
                    self.enemiesBullets.append(bulletAdd)
        else:
            rnd = random.randint(0,20)
            if rnd == 10:
                bulletAdd = self.Boss.shoot()
                self.enemiesBullets.append(bulletAdd) 
            
    def checkCollisonCircle(self,Coords1:[],Coords2:[],Rad1:int,Rad2:int) -> bool:
        #find the distance between the 2 center points of the circles
        distance = math.sqrt(math.pow(Coords1[0] - Coords2[0],2) + math.pow(Coords1[1] - Coords2[1],2))

        if distance <= Rad1+Rad2: #Checks if they are colliding
            return True
        return False
    
    def GameOver(self) -> None:
        self.renderCenterText("Game Over!",(255,0,0))
        self.renderCenterText("Score: " + str(self.score),(50,205,50),50)
        self.renderCenterText("Click to Restart",(255,255,255),100)

    def StartScreen(self) -> None:
        self.renderCenterText("Intergalatic",(0,255,255))
        self.renderCenterText("Click to Start!",(255,255,255),50)
    
    def renderCenterText(self,text,rgb,offset = 0) -> None:
        font = pygame.freetype.SysFont("Comic Sans MS",28)
        fontWidth = font.get_rect(text)
        font.render_to(self.win,(self.center - fontWidth.width / 2,(self.height / 3) + offset),text,rgb)

    def moveBullets(self) -> None:
        for bulletIndex,bullet in enumerate(self.bullets): #Iterates through all of the projectiles
            bullet.moveBullet()
            
            if not self.isBossRound:
                for enemyIndex,target in enumerate(self.enemies): #Iterates through all enemies to see if a projectile hit it
                    if self.checkCollisonCircle([target.getX(),target.getY()],[bullet.getX(),bullet.getY()],target.getRad(),bullet.getRad()):
                        if self.enemies[enemyIndex].hasCoin:
                            self.coins.append(Coin(100,(255,255,0),self.enemies[enemyIndex].getX(),self.enemies[enemyIndex].getY(),5))

                        del self.enemies[enemyIndex] #Deletes the Enemy
                        del self.bullets[bulletIndex] #Deletes the Bullet
                        
                        self.addScore(100)
            else:
                if len(self.Boss.minionList) == 0:

                    if self.checkCollisonCircle([self.Boss.getX(),self.Boss.getY()],[bullet.getX(),bullet.getY()],self.Boss.getRad(),bullet.getRad()):
                        self.Boss.health -= 1 #subtracts Boss Health

                        if self.Boss.health <= 0:
                            self.addScore(1500)
                            self.coins.append(BossToken(500,(255,165,0),self.Boss.getX(),self.Boss.getY(),15))
                            self.Boss = None
                            self.isBossRound = False
                        del self.bullets[bulletIndex] #Deletes the Bullet
                        
                else:
                    for index,item in enumerate(self.Boss.minionList):
                        if self.checkCollisonCircle([item.getX(),item.getY()],[bullet.getX(),bullet.getY()],item.getRad(),bullet.getRad()):
                            item.health -= 1
                            if item.health <= 0:
                                del self.Boss.minionList[index]
                            del self.bullets[bulletIndex]

            if bullet.getY() <= 0:
                del self.bullets[bulletIndex]
            else:
                bullet.drawBullet(self.win)

    def moveEnemyBullets(self) -> None:
        for enemyBulIndex, bullet in enumerate(self.enemiesBullets):
            bullet.moveBullet()
                        
            if self.checkCollisonCircle([bullet.getX(),bullet.getY()],[self.player.getX(),self.player.getY()],bullet.getRad(),self.player.getRad()):
                del self.enemiesBullets[enemyBulIndex]
                self.player.health -= 1
            if self.player.health <= 0:
                self.gameOver = True
            else:   
                bullet.drawBullet(self.win)
                
    def moveCoin(self) -> None:
        if len(self.coins) > 0:
            for coinIndex, coin in enumerate(self.coins):
                coin.moveCoin()
            
                if self.checkCollisonCircle([self.player.getX(),self.player.getY()],[coin.getX(),coin.getY()],self.player.getRad(),coin.getRad()):
                    if type(coin) is BossToken:
                        self.player.totalBossTokens += 1

                    self.addScore(coin.getVal())
                    del self.coins[coinIndex]
                
                coin.drawCoin(self.win)
            
    def needMoreEnemy(self) -> bool:
        if len(self.enemies) <= 0 or self.isBossRound and self.Boss == None:
            return True
        return False

    def draw(self) -> None: #also functions as the update method
        self.moveBullets()
        self.moveEnemyBullets()
        self.moveCoin()
                
        if not self.gameOver:
            if self.needMoreEnemy(): #Checks if more enemies need to be put on screen
                if self.player.health < 5:
                    self.player.health += 1
                self.round += 1
                if self.round % 5 == 0:
                    self.isBossRound = True
                    self.makeBoss()
                else:
                    self.makeEnemies()
                    
            if self.isBossRound: #Draws the boss if it is a boss round
                self.Boss.changeColor()
                self.Boss.drawEnemy(self.win)
                for item in self.Boss.minionList:
                    item.changeColor()
                    item.drawEnemy(self.win)
            else:
                for index,item in enumerate(self.enemies): #Draws all of the Enemies
                    item.drawEnemy(self.win)

            self.renderLables()
            self.player.drawPlayer(self.win)
