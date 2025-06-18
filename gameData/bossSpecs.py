from bullet import *
#Goliath Boss Funcs

def goliathSpec(self):
    if self.health < self.maxHp:
        self.health += 3
    return []

#Overseer Boss Funcs

def overseerExtraData(self):
    self.minionList = []

def overseerSpec(self):
    return []

#Rouge Boss Funcs

def rougeSpec(self):
    return [KillBullet(self.getX(),self.getY() + self.rad,velocity=[0,7.5],bulletSprite=("sprites/KillBullet.png",30,30))]