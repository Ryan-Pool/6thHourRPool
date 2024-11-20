#Name: Ryan Pool
#Class: 6th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all the ratings.

#code to input models into game
def getModels():
    models = []

    while True:
        try:
            numModels = int(input("Please enter number of models: "))
            break
        except ValueError:
            print("Invalid input please enter a valid number: ")

    for i in range(numModels):
        print(f"\nEnter a name for model {i + 1}: ")
        modelName = input("Name: ")
        models.append(modelName)

    return models

#code for scores of models
def modelScore():
    while True:
        try:
            numOfScore = int(input(f"Enter score (1-5): "))
            if 1 <= numOfScore <= 5:
                return numOfScore
            else:
                print(f"Score must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

#code to find average of the ratings
#To find the average add all inputs together and divide by total
def rateModels():
    models = getModels()
    totalScore = 0

    print("\nRate each model:")
    for model in models:
        print(f"\nRating for model: {model}")
        score = modelScore()
        totalScore += score

    overallAverage = totalScore / len(models) if models else 0
    print(f"Overall Average Score of All Models = {overallAverage:.2f}")

#Run the code
if __name__ == "__main__":
    rateModels()
