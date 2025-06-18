from gameData.formationFuncs import *

FORMATION_DATA = {
    "SquareForm":{
        "name":"SquareForm",
        "funcName":squareFormFunc,
        "spacing":50
    },
    "DiamondForm":{
        "name":"DiamondForm",
        "funcName":diamondFormFunc,
        "spacing":35
    }
}

BOSS_FORMATION_DATA = {
    "GoliathForm":{
        "name":"Goliath",
        "funcName":goliathFormFunc,
        "spacing":120
    },
    "RougeForm":{
        "name":"Rouge",
        "funcName":rougeFormFunc,
        "spacing":120
    },
    "HiveForm":{
        "name":"Hive Mind",
        "funcName":hiveFormFunc,
        "spacing":120
    }
}