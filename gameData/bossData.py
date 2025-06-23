import random as rnd
from gear import *
from formation import *
from gameData.bossSpecs import *

ROUND_MOD = 5

def No_Spec_Data(self):#Used as a placeholder if a boss or enemy doesnt have extra values
    return []

def Can_Be_Hurt_Always(self):
    return True

BOSS_DATA_ARRAY:dict = {
    "BGOL":{
        "name":'Goliath',
        "maxHp":lambda round:50 + int(round/ ROUND_MOD),
        "hp":lambda round:45 + int(round / ROUND_MOD),
        "xp":lambda round:150 * int(round / ROUND_MOD),
        "sprite":{
            "path":"sprites/Goliath.png",
            "width":60,
            "height":60
        },
        "speed":5,
        "coinOdds":lambda:True,
        "fireRate":40,
        "specRate":250,
        "scoreVal":300,
        "gear":"DoubleShot",
        "special":goliathSpec,
        "can_be_hurt":Can_Be_Hurt_Always,
    },
    "BOVS":{
        "name":'Overseer',
        "maxHp":lambda round:20 + int(round/ ROUND_MOD),
        "hp":lambda round:20 + int(round / ROUND_MOD),
        "xp":lambda round:100 * int(round / ROUND_MOD),
        "sprite":{
            "path":"sprites/Hive.png",
            "width":60,
            "height":60
        },
        "speed":5,
        "coinOdds":lambda:True,
        "fireRate":40,
        "specRate":250,
        "scoreVal":300,
        "gear":"DoubleShot",
        "special":overseerSpec,
        "can_be_hurt":overseerCanBeHurt,
    },
    "BRGE":{
        "name":'Rouge',
        "maxHp":lambda round:15 + int(round/ ROUND_MOD),
        "hp":lambda round:15 + int(round / ROUND_MOD),
        "xp":lambda round:100 * int(round / ROUND_MOD),
        "sprite":{
            "path":"sprites/Rouge.png",
            "width":60,
            "height":60
        },
        "speed":5,
        "coinOdds":lambda:True,
        "fireRate":30,
        "specRate":100,
        "scoreVal":300,
        "gear":"TripleShot",
        "special":rougeSpec,
        "can_be_hurt":Can_Be_Hurt_Always,
    },
    "BTFG":{
        "name":'Telefrag',
        "maxHp":lambda round:30 + int(round/ ROUND_MOD),
        "hp":lambda round:30 + int(round / ROUND_MOD),
        "xp":lambda round:100 * int(round / ROUND_MOD),
        "sprite":{
            "path":"sprites/Telefrag.png",
            "width":60,
            "height":60
        },
        "speed":5,
        "coinOdds":lambda:True,
        "fireRate":75,
        "specRate":75,
        "scoreVal":400,
        "gear":"MachineGun",
        "special":teleSpec,
        "can_be_hurt":Can_Be_Hurt_Always,
    },
}