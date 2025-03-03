#Name:
#Class: 6th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).

sportDict = {
    "sport1": {
        "Name" : "Volleyball",
        "Players" : 6,
        "Ball" : True
    },
    "sport2": {
        "Name" : "Soccer",
        "Players" : 11,
        "Ball" : True
    },
    "sport3": {
        "Name" : "Solo Figure Skating",
        "Players" : 1,
        "Ball" : False
    }
}

#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum

def sumSport():
    print(sportDict["sport1"]["Players"] + sportDict["sport2"]["Players"] + sportDict["sport3"]["Players"])

#3. Call the function with arguments here
sumSport()