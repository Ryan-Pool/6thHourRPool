#Name: Ryan Pool
#Class: 6th Hour
#Assignment: HW18
import random
from timeit import repeat


#1. Import the "random" library and create a def function that prints "Hello World!"
def helloWorld():
    print("Hello World")

#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["white", "yellow", "red", "green", "gray"]

#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def beanSelect():
    bean = random.choice(beanBag)
    print(bean)

    beanBag.remove(bean)

    repeatGame()

#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def repeatGame():
    userInput = input("Would you like to play again? Y/N ")
    if userInput == "Y" or userInput == "y":
        beanSelect()
    elif userInput == "N" or userInput == "n":
        exit()
    else:
        print("Invalid input")
        repeatGame()

#5. Call the #3 function at the bottom.
beanSelect()