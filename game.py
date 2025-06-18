import math
import pygame as PyGame
import pygame.freetype as PyFreeType
from random import randint,choice
from player import Player
from coin import *
from bullet import *
from enemy import *
from gear import *
from formation import *
from gameData.enemyData import *
from gameData.bossData import *
from gameData.formationData import *
from gameData.gearData import *
from const import HEIGHT

class Game():
    def __init__(self,screen:PyGame.Surface,center:float,height:float) -> None:
        self.SCREENCENTER:float = center
        self.win:Surface = screen
        self.player:Player = Player(center,height - 75,25) #Sets the player to spawn in the center of the screen towards the bottom
        self.height:float = height
        self.center:float = center
        self.bullets:list = []
        self.enemies:Formation = Formation(self.center * 2,self.height,FORMATION_DATA['SquareForm'])
        self.enemiesBullets:list = []
        self.coins:list = []
        self.shootState:bool = True
        self.score:int = 0
        self.gameOver:bool = False
        self.startGame:bool = False
        self.round:int = 1
        self.gearSelectNum:int = 0
        self.font = PyFreeType.Font("PixelifySans-VariableFont_wght.ttf",32)
        
        self.isBossRound:bool = False

        self.makeEnemies()

    def renderLables(self) -> None: #Renders game labels
      
        self.font.render_to(self.win,(5,5),"Score: " + str(self.score),(255,255,255))
        
        self.font.render_to(self.win,(350,5),"Multiplier: X" + str(round(self.player.getScoreMultiplyer(),1)),(255,255,255))
        
        self.font.render_to(self.win,(5,HEIGHT - 22),"Health: " + str(self.player.health) + "/" + str(self.player.maxHealth),(255,255,255))

        if self.isBossRound:
            bossHealth = self.enemies.getBossHealth()
            self.font.render_to(self.win,(150,47), self.enemies.getBossName() + " Health: " + str(bossHealth[1]) + "/" + str(bossHealth[0]),(255,0,0))
        
        
    def addScore(self,scoreAmt:int) -> None: #Adds points to the player's score
        self.score += math.floor(scoreAmt * self.player.getScoreMultiplyer())
        
    def handleInput(self) -> None: #Self Explanatory
        keys:list = PyGame.key.get_pressed()

        if keys[PyGame.K_LEFT]:
            self.player.movePlayer(-5)
               
        if keys[PyGame.K_RIGHT]:
            self.player.movePlayer(5)
            
        if keys[PyGame.K_UP] and self.shootState: 
            bulletAdd:list = []
            bulletAdd = self.player.shoot()
                
            for bullet in bulletAdd:
                self.bullets.append(bullet)
            self.shootState = False

    def changeShootState(self,state:bool) -> None: #Player can't hold to shoot, have to hit the fire button every time
        self.shootState = state
        
    def makeEnemies(self) -> None: #Filles the enemy array
        formChoose = choice(list(FORMATION_DATA.items()))
        self.enemies = Formation(self.center * 2,self.height,formChoose[1],self.round)
        self.enemies.createFormation(self.center)

    def makeBoss(self) -> None: #Creates the boss object
        formChoose = choice(list(BOSS_FORMATION_DATA.items()))
        self.enemies = Formation(self.center * 2,self.height,formChoose[1],self.round)
        self.enemies.createFormation(self.center)
        
    def getBoss(self,x,y,rad) -> Boss: #Obtains a random boss
        bossChoose = choice(list(BOSS_DATA_ARRAY.items()))
        return Boss(x,y,rad,bossChoose[1],self.round)
                
    def moveEnemies(self) -> None:
        self.enemies.update()
               
    def enemyShoot(self) -> None: #Spawns the enemy bullets and activates boss specials
        bulletCheck:list = []
        bulletCheck = self.enemies.enemyShoot()
                
        for item in bulletCheck:
            if type(item) is not None:
                self.enemiesBullets.append(item)
            
    def checkCollisonCircle(self,Coords1:list,Coords2:list,Rad1:int,Rad2:int) -> bool: #Checks if 2 circles collided
        #find the distance between the 2 center points of the circles
        distance:float = math.sqrt(math.pow(Coords1[0] - Coords2[0],2) + math.pow(Coords1[1] - Coords2[1],2))

        if distance <= Rad1+Rad2: #Checks if they are colliding
            return True
        return False
    
    def GameOver(self) -> None: #Renders labels at game over
        self.renderCenterText("Game Over!",(255,0,0))
        self.renderCenterText("Score: " + str(self.score),(50,205,50),50)
        self.renderCenterText("Click to Restart",(255,255,255),100)
         
    def StartScreen(self) -> None: #Renders labels at the start
        self.renderCenterText("Intergalatic",(0,128,255),-100,128)
        self.renderCenterText("Click to Start!",(255,255,255),35)
        self.renderCenterText("Selected Gear: " + self.player.gear.getName(),(255,255,255),125)
        self.renderCenterText("Hit R to Change!",(255,255,255),175)
    
    def renderCenterText(self,text:str,rgb:tuple,offset:int = 0,fontSize: int = 28) -> None: #Function that renders labels at the center
        fontWidth:int = self.font.get_rect(text)
        self.font.render_to(self.win,(self.center - fontWidth.width / 2,(self.height / 3) + offset),text,rgb)

    def gearSelect(self) -> None: #Allows the player to select gear
        self.gearSelectNum += 1
        
        gearList = list(GEAR_DATA.items())
        if self.gearSelectNum > len(gearList) - 1:
            self.gearSelectNum = 0
        
        self.player.gear = Gear(gearList[self.gearSelectNum][1])

    def moveBullets(self) -> None:
        for bulletIndex,bullet in enumerate(self.bullets): #Iterates through all of the projectiles
            bullet.moveBullet()
        
            for enemyIndex,target in enumerate(self.enemies.enemyList): #Iterates through all enemies to see if a projectile hit it
                if self.checkCollisonCircle([target.getX(),target.getY()],[bullet.getX(),bullet.getY()],target.getRad(),bullet.getRad()):
                    if self.enemies.enemyList[enemyIndex].hasCoin and self.enemies.enemyList[enemyIndex].health - 1 <= 0:
                        if type(self.enemies.enemyList[enemyIndex]) is Boss:
                            self.coins.append(BossToken(200,self.enemies.enemyList[enemyIndex].getX(),self.enemies.enemyList[enemyIndex].getY(),5))
                        else:
                            rndUpgrade = randint(1,3)
                            if rndUpgrade == 3:
                                self.coins.append(UpgradeToken(200,self.enemies.enemyList[enemyIndex].getX(),self.enemies.enemyList[enemyIndex].getY(),5))
                            else:
                                self.coins.append(Coin(100,self.enemies.enemyList[enemyIndex].getX(),self.enemies.enemyList[enemyIndex].getY(),5))
                    try:
                        self.enemies.enemyList[enemyIndex].health -= self.player.gear.dmg
                        if self.enemies.enemyList[enemyIndex].health <= 0:
                            self.addScore(self.enemies.enemyList[enemyIndex].scoreVal)

                            del self.enemies.enemyList[enemyIndex] #Deletes the Enemy
                        if len(self.bullets) != 0: #bullet list is sometimes zero and breaks so this prevents it
                            if bullet.pierce <= 0 or bullet.getY() <= 0:
                                del self.bullets[bulletIndex] #Deletes the Bullet
                            else:
                                bullet.pierce -= 1
                        
                    except IndexError as ex: #This Shouldn't Fire, Hopefully
                        print(ex)
            if bullet.getY() <= 0:
                del self.bullets[bulletIndex] #Removes a bullet if it gets off screen
            else:
                bullet.drawBullet(self.win)

    def killBoss(self):
        self.addScore(1500)
        self.player.upgrade()
        self.isBossRound = False

    def moveEnemyBullets(self) -> None: #Moves the enemy projectiles and cheks if they collided with the player
        for enemyBulIndex, bullet in enumerate(self.enemiesBullets):
            bullet.moveBullet()

            if not bullet.getY() > self.height:   
                if self.checkCollisonCircle([bullet.getX(),bullet.getY()],[self.player.getX(),self.player.getY()],bullet.getRad(),self.player.getRad()):
                    if type(bullet) is KillBullet: #Kill Bullets one shot the player
                        del self.enemiesBullets[enemyBulIndex]
                        self.player.health = 0
                    else:
                        del self.enemiesBullets[enemyBulIndex]
                        self.player.health -= 1
                    
                if self.player.health <= 0:
                    self.gameOver = True
                else:   
                    bullet.drawBullet(self.win)
            else:
                del self.enemiesBullets[enemyBulIndex]
                
    def moveCoin(self) -> None:#Moves coins and boss tokens. Updates score if they are collected
        if len(self.coins) > 0:
            for coinIndex, coin in enumerate(self.coins):
                coin.moveCoin()
            
                if self.checkCollisonCircle([self.player.getX(),self.player.getY()],[coin.getX(),coin.getY()],self.player.getRad(),coin.getRad()):
                    if type(coin) is BossToken:
                        self.player.totalBossTokens += 1
                    elif type(coin) is UpgradeToken:
                        self.player.upgrade()

                    self.addScore(coin.getVal())
                    del self.coins[coinIndex]
                
                coin.drawCoin(self.win)
            
    def needMoreEnemy(self) -> bool: #checks if all of the enemies are gone
        if len(self.enemies.enemyList) == 0:
            return True
        return False

    def update(self) -> None: #Updates the positions of all the objects and calles attack functions
        self.enemyShoot()
        self.moveEnemies()
        self.moveBullets()
        self.moveEnemyBullets()
        self.moveCoin()
        
    def incRound(self) -> None: #increases the round number and sets the boss round
        if self.player.health < 5:
            self.player.health += 1
            
        self.round += 1
        self.isBossRound = False
            
        if self.round % 5 == 0:
            self.isBossRound = True
            self.makeBoss()
        else:
            self.makeEnemies()     

    def draw(self) -> None:
        self.update()
                
        if not self.gameOver:
            if self.needMoreEnemy(): #Checks if more enemies need to be put on screen
                self.incRound()
            else: #Draws all of the Enemies
                 self.enemies.drawEnemies(self.win)

            self.renderLables()
            self.player.drawPlayer(self.win)