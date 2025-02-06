#Name: Ryan Pool
#Class: 6th Hour
#Assignment: Scenario 7

#Import all of Scenario 6 here
from Scenario6 import diceRoll, rollStat, statList

listAverage = 0

def final_average():
    global listAverage
    listAverage = sum(statList) / len(statList)
    return listAverage

final_average()

print(listAverage)