#Ryan Pool
#6th
#Scenario 2


#Scenario 2:
#The programmer in charge of the player character party stats is
#having some issues with their code. Despite rigorous testing,
#they are inexperienced and can't seem to figure out why it damage
#testing isn't working. Your team lead has asked you to help by fixing
#the party dictionary, insert an enemy into the code below, and
#testing to see if a player character can damage the with a printed
#test that shows the enemy health has changed.


partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
    }
}

#Enemy Dictionary goes here
enemyDict = {
    "enemy1" : {
       "Name" : "Taken",
        "Leader" : "Oryx the Taken King",
        "Location" : "Ascendant plane",
        "Damage" : 500,
        "Health" : 200
    },
    "enemy2" : {
        "Name" : "Cabal",
        "Leader" : "Calus",
        "Location" : "Ancient Rome",
        "Damage" : 400,
        "Health" : 500
    },
    "enemy3" : {
        "Name" : "Scorn",
        "Leader" : "Uldren Sov",
        "Location" : "Tangled Shore",
        "Damage" : 700,
        "Health" : 200
    },
    "enemy4" : {
        "Name" : "Vex",
        "Leader" : False,
        "Location" : "Europa",
        "Damage" : 200,
        "Health" : 500
    },
    "enemy5" : {
        "Name" : "Hive",
        "Leader" : "Worm God Xol",
        "Location" : "Savathun Throne World",
        "Damage" : 100,
        "Health" : 50
    }
}


#Test the damage here by subtracting a party member's damage from the enemy's health.
print("LaeZel vs. the Taken =", enemyDict["enemy1"]["Health"]-partyDictionary["LaeZel"]["Damage"])
print("Shadowheart vs. the Cabal =", enemyDict["enemy2"]["Health"]-partyDictionary["Shadowheart"]["Damage"])
print("Gale vs. the Scorn =", enemyDict["enemy3"]["Health"]-partyDictionary["Gale"]["Damage"])
print("Astarion vs. the Vex =", enemyDict["enemy4"]["Health"]-partyDictionary["Astarion"]["Damage"])
