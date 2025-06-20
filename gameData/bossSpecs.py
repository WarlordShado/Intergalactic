from bullet import *
from gear import *
from gameData.gearData import *
import Globals
import random as rnd
#Goliath Boss Funcs

def goliathSpec(self) -> list:
    if self.health < self.maxHp:
        self.health += 3
    return []

#Overseer Boss Funcs

def overseerSpec(self) -> list:
    return []

def overseerCanBeHurt(self) -> bool:
    if len(Globals.game.enemies.enemyList) == 1:
        return True
    return False

#Rouge Boss Funcs

def rougeSpec(self) -> list:
    return [KillBullet(self.getX(),self.getY() + self.rad,velocity=[0,7.5],bulletSprite=("sprites/KillBullet.png",30,30))]

#Telefrag Boss Funcs

def teleSpec(self) -> list:
    flipEnemyPos = rnd.randint(0,len(Globals.game.enemies.enemyList) - 1)

    bossX = self.getX()
    bossY = self.getY()
    enemyX = Globals.game.enemies.enemyList[flipEnemyPos].getX()
    enemyY = Globals.game.enemies.enemyList[flipEnemyPos].getY()

    self.x = enemyX
    self.y = enemyY
    Globals.game.enemies.enemyList[flipEnemyPos].x = bossX
    Globals.game.enemies.enemyList[flipEnemyPos].y = bossY

    gear = Gear(GEAR_DATA['TripleShot'],True)
    return gear.getBulletList(self.getX(),self.getY(),self.getRad())
    