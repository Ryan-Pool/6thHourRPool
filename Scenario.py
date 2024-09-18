#Ryan Pool
#6th Hour
#Scenario 1

enemyDict = {
    "enemy1" : {
       "Name" : "Taken",
        "Leader" : "Oryx the Taken King",
        "Location" : "Ascendant plane",
        "Damage" : 500
    },
    "enemy2" : {
        "Name" : "Cabal",
        "Leader" : "Calus",
        "Location" : "Ancient Rome",
        "Damage" : 400
    },
    "enemy3" : {
        "Name" : "Scorn",
        "Leader" : "Uldren Sov",
        "Location" : "Tangled Shore",
        "Damage" : 700
    },
    "enemy4" : {
        "Name" : "Vex",
        "Leader" : False,
        "Location" : "Europa",
        "Damage" : 200
    },
    "enemy5" : {
        "Name" : "Hive",
        "Leader" : "Worm God Xol",
        "Location" : "Savathun Throne World",
        "Damage" : 100
    }
}

enemyDict["enemy1"]["Damage"] = int(input("What amount of damage does the Hive do?: "))
enemyDict["enemy2"]["Damage"] = int(input("What amount of damage does the Taken do?: "))
enemyDict["enemy3"]["Damage"] = int(input("What amount of damage does the Cabal do?: "))
enemyDict["enemy4"]["Damage"] = int(input("What amount of damage does the Vex do?: "))
enemyDict["enemy5"]["Damage"] = int(input("What amount of damage does the Scorn do?: "))

print(enemyDict)