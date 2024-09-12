#Ryan Pool
#6th Hour
#HW4

print("Hello World")

pokemonDict = {
    "grass type" : "Leafeon",
    "fire type" : "Litten",
    "numbers" : [0,5,9]
}

print(pokemonDict["numbers"][1])

pokemonDict.update({"numbers2": 7})
print(pokemonDict)

pokemonDict.clear()
print(pokemonDict)

compSci = {
    "student1": {
        "Name": "Colin",
        "Grade": 12,
        "esports": True,
    },
    "student2": {
        "Name": "Ryan",
        "Grade": 12,
        "esports": True,
    },
    "student3": {
        "Name": "Sariah",
        "Grade": 12,
        "esports": False,
    }
}



print(compSci["student1"]["Name"],compSci["student2"]["Name"],compSci["student3"]["Name"])