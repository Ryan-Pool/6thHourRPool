#Ryan Pool
#6th Hour
#Scenario 3

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits, and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4

import random

#Party Dictionary Goes Here
partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : random.randint(2, 12) + 3,
        "Attack Modifier" : 3
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : random.randint(1, 6) + 2,
        "Attack Modifier" : 3
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : random.randint(1, 10),
        "Attack Modifier" : 3
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : random.randint(1, 6) + 4,
        "Attack Modifier" : 3
    }
}

#Enemy Dictionary Goes Here
enemyDict = {
    "enemy1" : {
       "Name" : "Taken",
        "Leader" : "Oryx the Taken King",
        "Location" : "Ascendant plane",
        "Damage" : random.randint(2, 10) + 2,
        "Health" : 6,
        "AC" : 10,
        "Attack Modifier" : 3
    },
    "enemy2" : {
        "Name" : "Cabal",
        "Leader" : "Calus",
        "Location" : "Ancient Rome",
        "Damage" : random.randint(1, 20) + 3,
        "Health" : 25,
        "AC" : 17,
        "Attack Modifier" : 7
    },
    "enemy3" : {
        "Name" : "Scorn",
        "Leader" : "Uldren Sov",
        "Location" : "Tangled Shore",
        "Damage" : random.randint(2, 12) + 2,
        "Health" : 18,
        "AC" : 15,
        "Attack Modifier" : 5
    },
    "enemy4" : {
        "Name" : "Vex",
        "Leader" : False,
        "Location" : "Europa",
        "Damage" : random.randint(2, 12) + 1,
        "Health" : 13,
        "AC" : 14,
        "Attack Modifier" : 4
    },
    "enemy5" : {
        "Name" : "Hive",
        "Leader" : "Worm God Xol",
        "Location" : "Savathun Throne World",
        "Damage" : random.randint(1, 14),
        "Health" : 11,
        "AC" : 16,
        "Attack Modifier" : 6
    }
}

#Combat Code Goes Here
#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits, and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#Enemy attack code
#Step 7: Roll the attack roll for party member (d20 + Attack Modifier)

enemy_d20Roll = random.randint(1, 20)#for rolling the d20 + the random attack

#Step 8: Check to see if the party member hits the enemy

if (enemy_d20Roll) + (enemyDict["enemy2"]["Attack Modifier"]) >= (partyDictionary["Astarion"]["AC"]):
    print("The Cabal hit Astarion")
    print("Astarion's health left: ", (enemyDict["enemy2"]["Damage"] - (partyDictionary)["Astarion"]["Health"]))
    if (partyDictionary["Astarion"]["Health"]) <= 0:
        print("Astarion died")
    else:
        print("Astarion is still alive")
        exit()
else:
    print("The Cabal missed Astarion")


party_d20Roll = random.randint(1, 20)#for rolling the d20 + the random attack


if (party_d20Roll) + (partyDictionary["Astarion"]["Attack Modifier"]) >= (enemyDict["enemy2"]["AC"]):
    print("Astarion hits the Cabal")
    print("The Cabal's health left: ", (partyDictionary["Astarion"]["Damage"] - (enemyDict)["enemy2"]["Health"]))
    if (enemyDict["enemy2"]["Health"]) <= 0:
        print("The Cabal died")
    else:
        print("The Cabal is alive")
        exit()
else:
    print("Astarion misses the Cabal")













