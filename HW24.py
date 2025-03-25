#Name: Ryan Pool
#Class: 6th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Characters:
    def __init__(self, name, health, damage, speed, max_health):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.max_health = health

    def damageDone(self):
        for i in range(10):
            time.sleep(1)
            self.health -= random.randint(1, 6)
            print(f"New health: {self.health}")

    def healDone(self):
        self.health += 30
        if self.health > 100:
            self.health = 100

#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
warrior = Characters("Warrior",100, 20, 30, 100)
healer = Characters("Healer",60, 10, 30, 60)
thief = Characters("Thief",50, 30, 40, 50)
mage = Characters("Mage",45, 35, 25, 45)

#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
choices = [warrior, healer, thief, mage]
randomChoice = random.choice(choices)

print(f"{randomChoice.name} got hit!")

randomChoice.damageDone()

#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
randomChoice.healDone()

print(f"{randomChoice.name} new health {randomChoice.health}")