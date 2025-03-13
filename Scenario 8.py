#Name: Ryan Pool
#Class: 6th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)

class Party:
    def __init__(self, health, AC, damage, attackModifier):
        self.health = health
        self.AC = AC
        self.damage = damage
        self.attackModifier = attackModifier

LaeZel = Party(12, 17, random.randint(2, 12) + 3, 3)
Shadowheart = Party(10, 14, random.randint(1, 6) + 2, 3)
Gale = Party(8, 14, random.randint(1, 10), 3)
Astarion = Party(10, 14, random.randint(1, 6) + 4, 3)
enemy1 = Party(6, 10, random.randint(2, 10) + 2, 3)
enemy2 = Party(25, 17, random.randint(1, 20) + 3, 7)
enemy3 = Party(18, 15, random.randint(2, 12) + 2, 5)
enemy4 = Party(13, 14, random.randint(2, 12) + 1, 4)
enemy5 = Party(11, 16, random.randint(1, 14), 6)


#Enemy attack code
#Step 7: Roll the attack roll for party member (d20 + Attack Modifier)

enemy_d20Roll = random.randint(1, 20)#for rolling the d20 + the random attack

#Step 8: Check to see if the party member hits the enemy

if enemy_d20Roll + enemy2.attackModifier >= Astarion.AC:
    print("The Cabal hit Astarion")
    print("Astarion's health left: ", enemy2.damage - Astarion.health)
    if Astarion.health <= 0:
        print("Astarion died")
    else:
        print("Astarion is still alive")
        exit()
else:
    print("The Cabal missed Astarion")


party_d20Roll = random.randint(1, 20)#for rolling the d20 + the random attack


if party_d20Roll + Astarion.attackModifier >= enemy2.AC:
    print("Astarion hits the Cabal")
    print("The Cabal's health left: ", Astarion.damage - enemy2.health)
    if enemy2.health <= 0:
        print("The Cabal died")
    else:
        print("The Cabal is alive")
        exit()
else:
    print("Astarion misses the Cabal")