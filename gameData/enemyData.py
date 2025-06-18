from gear import *
from gameData.bossSpecs import *
import random as rnd
ROUND_MOD = 5

ENEMY_DATA_ARRAY:dict = {
    "Basic_Enemy":{
        "hp":lambda round:3 + int(round / ROUND_MOD),
        "xp":lambda round:15 * (int(round / ROUND_MOD)+1),
        "sprite":{
            "path":"sprites/Enemy.png",
            "width":30,
            "height":30
        },
        "speed":5,
        "coinOdds":lambda:True if rnd.randint(1,5) == 1 else False,
        "fireRate":500,
        "scoreVal":100,
        "gear":"SingleShot"
    },
    "Strong_Enemy":{
        "hp":lambda round:6 + int(round / ROUND_MOD),
        "xp":lambda round:30 * (int(round / ROUND_MOD)+1),
        "sprite":{
            "path":"sprites/StrongEnemy.png",
            "width":30,
            "height":30
        },
        "speed":5,
        "coinOdds":lambda:True if rnd.randint(1,5) == 1 else False,
        "fireRate":500,
        "scoreVal":300,
        "gear":"SingleShot",
    },
    "Overseer_Minion":{
        "name":'Overseer_Minion',
        "maxHp":lambda round:4 + int(round/ ROUND_MOD),
        "hp":lambda round:4 + int(round / ROUND_MOD),
        "xp":lambda round:20 * (int(round / ROUND_MOD)+1),
        "sprite":{
            "path":"sprites/Minion.png",
            "width":30,
            "height":30
        },
        "speed":5,
        "coinOdds":lambda:False,
        "fireRate":250,
        "scoreVal":300,
        "gear":"SingleShot",
    }
}