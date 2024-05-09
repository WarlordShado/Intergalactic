import math
import pygame
import pygame.freetype
import random
from coin import *
from player import *
from bullet import *
from enemy import *
from gear import *

class Game():
    def __init__(self,screen:pygame.Surface,center:float,height:float) -> None:
        self.SCREENCENTER = center
        self.win = screen
        self.player = Player(center,height - 75,25) #Sets the player to spawn in the center of the screen towards the bottom
        self.height = height
        self.center = center
        self.bullets = []
        self.enemies = []
        self.enemiesBullets = []
        self.coins = []
        self.shootState = True
        self.score = 0
        self.gameOver = False
        self.startGame = False
        self.round = 1
        self.gearSelectNum = 0
        
        self.isBossRound = False
        self.Boss = None

        self.makeEnemies()

    def renderLables(self) -> None:
        font = pygame.freetype.SysFont("Comic Sans MS",32)
        font.render_to(self.win,(5,5),"Score: " + str(self.score),(255,255,255))
        
        font.render_to(self.win,(350,5),"Multiplyer: X" + str(round(self.player.getScoreMultiplyer(),1)),(255,255,255))
        
        font.render_to(self.win,(5,820),"Health: " + str(self.player.health) + "/5",(255,255,255))
        
        if self.isBossRound:
            font = pygame.freetype.SysFont("Comic Sans MS",32)
            font.render_to(self.win,(150,47), self.Boss.getName() + " Health: " + str(self.Boss.health) + "/" + str(self.Boss.maxHp),(255,0,0))
        
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
            if type(self.player.gear) is HomingStrike: #Deals with creating homing bullets
                if not self.isBossRound:
                    rnd = random.randint(0,len(self.enemies) - 1)
                    bulletAdd = self.player.shoot(self.enemies[rnd])
                else:
                    if type(self.Boss) is Overseer:
                        if len(self.Boss.minionList) != 0:
                            rnd = random.randint(0,len(self.Boss.minionList) - 1)
                            bulletAdd = self.player.shoot(self.Boss.minionList[rnd])
                        else:
                            bulletAdd = self.player.shoot(self.Boss)
                    else:
                        bulletAdd = self.player.shoot(self.Boss)
            else:
                bulletAdd = self.player.shoot()
                
            for bullet in bulletAdd:
                self.bullets.append(bullet)
            self.shootState = False

    def changeShootState(self,state:bool) -> None: #Player can't hold to shoot, have to hit the fire button every time
        self.shootState = state
        
    def makeEnemies(self) -> None: #Filles the enemy array
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
        self.Boss = self.getBoss(startX,startY,30)
        self.Boss.startSpecial(self.win)
        
    def getBoss(self,x,y,rad) -> Boss:
        rnd = random.randint(1,3)
        match rnd:
            case 1:
                return Overseer(x,y,rad)
            case 2:
                return Goliath(x,y,rad)
            case 3:
                return Rouge(x,y,rad)
                
    def moveEnemies(self) -> None:
        if not self.isBossRound: 
            for enemy in (self.enemies):
                enemy.moveEnemy()
                rnd = random.randint(1,10)
                if rnd == 5 :
                    enemy.reverseSpeed() #Makes the enemy switch directions
        else:
            self.Boss.moveEnemy()
            rnd = random.randint(1,10)
            if rnd == 5 :
                self.Boss.reverseSpeed()
               
    def enemyShoot(self) -> None:
        if not self.isBossRound:
            for enemy in (self.enemies):
                rnd = random.randint(0,enemy.fireRate) 
                if rnd == 10: #Random chance for the enemies to shoot
                    bulletAdd = enemy.shoot()
                    for item in bulletAdd:
                        self.enemiesBullets.append(item) 
        else:
            rndSpec = random.randint(0,self.Boss.specRate) #How Often the boss will use it's special move
            rndShoot = random.randint(0,self.Boss.fireRate) #Bosses have a very high change to shoot
            if rndShoot == 10:
                bulletAdd = self.Boss.shoot()
                for item in bulletAdd:
                    self.enemiesBullets.append(item) 
                
            if rndSpec == self.Boss.specRate // 2:
                if type(self.Boss) is Rouge:
                    bulletAdd = self.Boss.special(self.win,self.player)
                else:
                    bulletAdd = self.Boss.special()

                if bulletAdd is not None:
                    for item in bulletAdd:
                        self.enemiesBullets.append(item)
            
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
        self.renderCenterText("Intergalatic",(0,255,255),-100,64)
        self.renderCenterText("Click to Start!",(255,255,255),35)
        self.renderCenterText("Selected Gear: " + self.player.gear.getName(),(255,255,255),125)
        self.renderCenterText("Hit R to Change!",(255,255,255),175)
    
    def renderCenterText(self,text:str,rgb:(),offset:int = 0,fontSize: int = 28) -> None:
        font = pygame.freetype.SysFont("Comic Sans MS",fontSize)
        fontWidth = font.get_rect(text)
        font.render_to(self.win,(self.center - fontWidth.width / 2,(self.height / 3) + offset),text,rgb)

    def gearSelect(self) -> None:
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
                self.player.gear = HomingStrike()
            case 6:
                self.player.gear = Sniper()
                self.gearSelectNum = 0

    def moveBullets(self) -> None:
        for bulletIndex,bullet in enumerate(self.bullets): #Iterates through all of the projectiles
            bullet.moveBullet()
            bullet.update()
            
            if not self.isBossRound: #If it isnt a boss round, check if bullets hit the enemies
                for enemyIndex,target in enumerate(self.enemies): #Iterates through all enemies to see if a projectile hit it
                    if self.checkCollisonCircle([target.getX(),target.getY()],[bullet.getX(),bullet.getY()],target.getRad(),bullet.getRad()):
                        if self.enemies[enemyIndex].hasCoin:
                            self.coins.append(Coin(100,self.enemies[enemyIndex].getX(),self.enemies[enemyIndex].getY(),5))
                            
                        del self.enemies[enemyIndex] #Deletes the Enemy
                        if len(self.bullets) != 0: #bullet list is sometimes zero and breaks so this prevents it
                            if bullet.pierce == 0:
                                del self.bullets[bulletIndex] #Deletes the Bullet
                            else:
                                bullet.pierce -= 1
                        
                        self.addScore(100)
            else:
                if self.Boss.canBeHurt(): #Boss can't be hurt untile all minions are gone

                    if self.checkCollisonCircle([self.Boss.getX(),self.Boss.getY()],[bullet.getX(),bullet.getY()],self.Boss.getRad(),bullet.getRad()):
                        self.Boss.health -= self.player.gear.dmg

                        if self.Boss.health <= 0: #Means the boss died
                            self.addScore(1500)
                            self.coins.append(BossToken(500,self.Boss.getX(),self.Boss.getY(),15)) #Adds a boss token to the coin list
                            self.Boss = None 
                            self.isBossRound = False
                        del self.bullets[bulletIndex] #Deletes the Bullet if it collided with something
                elif type(self.Boss) is Overseer:
                    for index,item in enumerate(self.Boss.minionList): #If it is a boss round, the boss minions need to be checked
                        if self.checkCollisonCircle([item.getX(),item.getY()],[bullet.getX(),bullet.getY()],item.getRad(),bullet.getRad()):
                            item.health -= 1
                            if item.health <= 0:
                                del self.Boss.minionList[index]
                                self.addScore(300)
                            del self.bullets[bulletIndex]

            if bullet.getY() <= 0:
                del self.bullets[bulletIndex] #Removes a bullet if it gets off screen
            else:
                bullet.drawBullet(self.win)

    def moveEnemyBullets(self) -> None:
        for enemyBulIndex, bullet in enumerate(self.enemiesBullets):
            bullet.moveBullet()
                        
            if self.checkCollisonCircle([bullet.getX(),bullet.getY()],[self.player.getX(),self.player.getY()],bullet.getRad(),self.player.getRad()):
                if type(bullet) is KillBullet:
                    del self.enemiesBullets[enemyBulIndex]
                    self.player.health = 0
                else:
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
            
    def needMoreEnemy(self) -> bool: #checks if all of the enemies are gone
        if len(self.enemies) <= 0 or self.isBossRound and self.Boss == None:
            return True
        return False

    def update(self) -> None:
        self.moveBullets()
        self.moveEnemyBullets()
        self.moveCoin()

    def draw(self) -> None:
        self.update()
                
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
                if type(self.Boss) is Overseer:
                    for item in self.Boss.minionList:
                        item.changeColor()
                        item.drawEnemy(self.win)
            else:
                for index,item in enumerate(self.enemies): #Draws all of the Enemies
                    item.drawEnemy(self.win)

            self.renderLables()
            self.player.drawPlayer(self.win)