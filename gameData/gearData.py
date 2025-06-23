from gameData.gearFuncs import *

defBulletSprite = lambda x:{
            "path":"sprites/BasicBullet.png",
            "width":10,
            "height":10
        } if x == False else {
            "path":"sprites/EnemyBullet.png",
            "width":10,
            "height":10
        }

GEAR_DATA = {
    "SingleShot":{
        "name":"Single Shot",
        "bulletAmt":1,
        "radius":5,
        "fireRate":200,
        "damage":3,
        "pierce":0,
        "velocity":10,
        "bulletSprite":defBulletSprite,
        "fireFunc":singleShot,
        "lvlFunc":singleShotLvl
    },
    "DoubleShot":{
        "name":"Twin Strike",
        "bulletAmt":2,
        "radius":5,
        "fireRate":300,
        "damage":2,
        "pierce":1,
        "velocity":10,
        "bulletSprite":defBulletSprite,
        "fireFunc":doubleShot,
        "lvlFunc":doubleShotLvl
    },
    "TripleShot":{
        "name":"Fullisade",
        "bulletAmt":3,
        "radius":5,
        "fireRate":500,
        "damage":2,
        "pierce":0,
        "velocity":10,
        "bulletSprite":defBulletSprite,
        "fireFunc":tripleShot,
        "lvlFunc":tripleShotLvl
    },
    "MachineGun":{
        "name":"MachineGun",
        "bulletAmt":1,
        "radius":5,
        "fireRate":75,
        "damage":1,
        "pierce":0,
        "velocity":10,
        "bulletSprite":defBulletSprite,
        "fireFunc":machineGun,
        "lvlFunc":machineGunLvl
    },
    "Sniper":{
        "name":"Sniper",
        "bulletAmt":1,
        "radius":7,
        "fireRate":750,
        "damage":6,
        "pierce":2,
        "velocity":30,
        "bulletSprite":lambda x:{
            "path":"sprites/SniperRound.png",
            "width":14,
            "height":14
        },
        "fireFunc":sniper,
        "lvlFunc":sniperLvl
    }
}