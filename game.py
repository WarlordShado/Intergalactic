import math
import pygame
import pygame.freetype
import random
from coin import *
from player import *
from bullet import *
from enemy import *
from gear import *
from formation import *

class Game():
    def __init__(self,screen:pygame.Surface,center:float,height:float) -> None:
        self.SCREENCENTER = center
        self.win = screen
        self.player = Player(center,height - 75,25) #Sets the player to spawn in the center of the screen towards the bottom
        self.height = height
        self.center = center
        self.bullets = []
        self.enemies = Formation(self.center * 2,self.height)
        self.enemiesBullets = []
        self.coins = []
        self.shootState = True
        self.score = 0
        self.gameOver = False
        self.startGame = False
        self.round = 1
        self.gearSelectNum = 0
        self.font = pygame.freetype.Font("PixelifySans-VariableFont_wght.ttf",32)
        
        self.isBossRound = False
        self.BossFormation = None

        self.makeEnemies()

    def renderLables(self) -> None: #Renders game labels
      
        self.font.render_to(self.win,(5,5),"Score: " + str(self.score),(255,255,255))
        
        self.font.render_to(self.win,(350,5),"Multiplier: X" + str(round(self.player.getScoreMultiplyer(),1)),(255,255,255))
        
        self.font.render_to(self.win,(5,820),"Health: " + str(self.player.health) + "/5",(255,255,255))
        
        if self.isBossRound:
            self.font.render_to(self.win,(150,47), self.BossFormation.Boss.getName() + " Health: " + str(self.BossFormation.Boss.health) + "/" + str(self.BossFormation.Boss.maxHp),(255,0,0))
        
    def addScore(self,scoreAmt:int) -> None: #Adds points to the player's score
        self.score += math.floor(scoreAmt * self.player.getScoreMultiplyer())
        
    def handleInput(self) -> None: #Self Explanatory
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.movePlayer(-5)
               
        if keys[pygame.K_RIGHT]:
            self.player.movePlayer(5)
            
        if keys[pygame.K_UP] and self.shootState: 
            bulletAdd = []
            bulletAdd = self.player.shoot()
                
            for bullet in bulletAdd:
                self.bullets.append(bullet)
            self.shootState = False

    def changeShootState(self,state:bool) -> None: #Player can't hold to shoot, have to hit the fire button every time
        self.shootState = state
        
    def makeEnemies(self) -> None: #Filles the enemy array
        rnd = random.randint(1,2)
        match rnd:
            case 1:
                self.enemies = SquareForm(self.center * 2,self.height)
            case 2:
                self.enemies = DiamondForm(self.center * 2,self.height)

        self.enemies.createFormation(self.center)
                
    def makeBoss(self) -> None: #Creates the boss object
        startX = self.SCREENCENTER
        startY = 125
        BossType = self.getBoss(startX,startY,30)
        if type(BossType) is Overseer:
            self.BossFormation = HiveFormation(self.center * 2,self.height,BossType)
            self.BossFormation.createFormation(self.center)
        else:
            self.BossFormation = BossFormation(self.center * 2,self.height,BossType)
            
        
    def getBoss(self,x,y,rad) -> Boss: #Obtains a random boss
        rnd = random.randint(1,4)
        match rnd:
            case 1:
                return Overseer(x,y,rad)
            case 2:
                return Goliath(x,y,rad)
            case 3:
                return Rouge(x,y,rad)
            case 4: 
                return Teleporter(x,y,rad,self.center * 2)
                
    def moveEnemies(self) -> None:
        if not self.isBossRound: 
            self.enemies.update()
        else:
            self.BossFormation.update()
               
    def enemyShoot(self) -> None: #Spawns the enemy bullets and activates boss specials
        bulletAdd = []
        bulletCheck = []

        if not self.isBossRound:
            bulletCheck = self.enemies.enemyShoot()
        else:
            bulletCheck = self.BossFormation.enemyShoot()
            specCheck = self.BossFormation.useSpecial(self.win)
            
            for item in specCheck:
                if type(item) is not None:
                    self.enemiesBullets.append(item)
                
        for item in bulletCheck:
            if type(item) is not None:
                self.enemiesBullets.append(item)
            
    def checkCollisonCircle(self,Coords1:list,Coords2:list,Rad1:int,Rad2:int) -> bool: #Checks if 2 circles collided
        #find the distance between the 2 center points of the circles
        distance = math.sqrt(math.pow(Coords1[0] - Coords2[0],2) + math.pow(Coords1[1] - Coords2[1],2))

        if distance <= Rad1+Rad2: #Checks if they are colliding
            return True
        return False
    
    def GameOver(self) -> None: #Renders labels at game over
        self.renderCenterText("Game Over!",(255,0,0))
        self.renderCenterText("Score: " + str(self.score),(50,205,50),50)
        self.renderCenterText("Click to Restart",(255,255,255),100)
         
    def StartScreen(self) -> None: #Renders labels at the start
        self.renderCenterText("Intergalatic",(0,255,255),-100,64)
        self.renderCenterText("Click to Start!",(255,255,255),35)
        self.renderCenterText("Selected Gear: " + self.player.gear.getName(),(255,255,255),125)
        self.renderCenterText("Hit R to Change!",(255,255,255),175)
    
    def renderCenterText(self,text:str,rgb:(),offset:int = 0,fontSize: int = 28) -> None: #Function that renders labels at the center
        fontWidth = self.font.get_rect(text)
        self.font.render_to(self.win,(self.center - fontWidth.width / 2,(self.height / 3) + offset),text,rgb)

    def gearSelect(self) -> None: #Allows the player to select gear
        self.gearSelectNum += 1
        match self.gearSelectNum:
            case 1:
                self.player.gear = Gear()
            case 2:
                self.player.gear = DoubleShot()
            case 3:
                self.player.gear = TripleShot()
            case 4:
                self.player.gear = MachineGun()
            case 5:
                self.player.gear = Sniper()
            case 6:
                self.player.gear = BlackHole()
                self.gearSelectNum = 0 #Resets the match case

    def moveBullets(self) -> None:
        for bulletIndex,bullet in enumerate(self.bullets): #Iterates through all of the projectiles
            bullet.moveBullet()
            
            if not self.isBossRound: #If it isnt a boss round, check if bullets hit the enemies
                for enemyIndex,target in enumerate(self.enemies.enemyList): #Iterates through all enemies to see if a projectile hit it
                    if self.checkCollisonCircle([target.getX(),target.getY()],[bullet.getX(),bullet.getY()],target.getRad(),bullet.getRad()):
                        if self.enemies.enemyList[enemyIndex].hasCoin and self.enemies.enemyList[enemyIndex].health - 1 <= 0:
                            self.coins.append(Coin(100,self.enemies.enemyList[enemyIndex].getX(),self.enemies.enemyList[enemyIndex].getY(),5))
                        try:
                            self.enemies.enemyList[enemyIndex].health -= 1
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
            else:
                if self.BossFormation.Boss.canBeHurt(): #Boss can't be hurt untile all minions are gone

                    if self.checkCollisonCircle([self.BossFormation.Boss.getX(),self.BossFormation.Boss.getY()],[bullet.getX(),bullet.getY()],self.BossFormation.Boss.getRad(),bullet.getRad()):
                        self.BossFormation.Boss.health -= self.player.gear.dmg

                        if self.BossFormation.Boss.health <= 0: #Means the boss died
                            self.killBoss()
                        del self.bullets[bulletIndex] #Deletes the Bullet if it collided with something
                elif type(self.BossFormation.Boss) is Overseer:
                    for index,item in enumerate(self.BossFormation.Boss.minionList): #If it is a boss round, the boss minions need to be checked
                        if self.checkCollisonCircle([item.getX(),item.getY()],[bullet.getX(),bullet.getY()],item.getRad(),bullet.getRad()):
                            item.health -= 1
                            if item.health <= 0:
                                del self.BossFormation.Boss.minionList[index]
                                self.addScore(300)
                            del self.bullets[bulletIndex]

            if bullet.getY() <= 0:
                del self.bullets[bulletIndex] #Removes a bullet if it gets off screen
            else:
                bullet.drawBullet(self.win)

    def killBoss(self):
        self.addScore(1500)
        self.coins.append(BossToken(500,self.BossFormation.Boss.getX(),self.BossFormation.Boss.getY(),15)) #Adds a boss token to the coin list
        self.BossFormation.Boss = None 
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

                    self.addScore(coin.getVal())
                    del self.coins[coinIndex]
                
                coin.drawCoin(self.win)
            
    def needMoreEnemy(self) -> bool: #checks if all of the enemies are gone
        if len(self.enemies.enemyList) == 0 or self.isBossRound and self.BossFormation == None:
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
            
        if self.round % 5 == 0:
            self.isBossRound = True
            self.makeBoss()
        else:
            self.makeEnemies()
                
    def updateBoss(self) -> None: #Changes the boss's color and draws it. if it summons stuff, it will draw that too
        self.BossFormation.drawEnemies(self.win)      

    def draw(self) -> None:
        self.update()
                
        if not self.gameOver:
            if self.needMoreEnemy(): #Checks if more enemies need to be put on screen
                self.incRound()
            if self.isBossRound: #Draws the boss if it is a boss round
                self.updateBoss()
            else: #Draws all of the Enemies
                 self.enemies.drawEnemies(self.win)

            self.renderLables()
            self.player.drawPlayer(self.win)