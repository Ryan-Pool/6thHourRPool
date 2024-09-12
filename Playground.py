#Ryan Pool
#Playground
#6th Hour

#The conversation between user and computer leading up to the game
userName = input("What is your name? ")
print("Hello",userName)

#Computer asking if user wants to play r p s
userResponse = input("Would you like to play Rock, Paper, Scissors? ")

#If user puts yes or no computer's response:
def determineAnswer(userResponse):
    if userResponse == 'Yes' or \
        userResponse == 'yes':
        return "Awesome! Please enter rock, paper, or scissors:"
    elif userResponse == 'No' or \
        userResponse == 'no':
        return "Too bad you will play anyway. Please enter rock, paper, or scissors:"
    else:
        return "I didn't understand that, but let's play anyway! Please enter rock, paper, or scissors:"

#print the computers response
response = determineAnswer(userResponse)
print(response)

#user choice for r p s
userChoice = input()

#Code to make users choice valid
choices = ['rock', 'paper', 'scissors']
while userChoice not in choices:
    print("invalid choice, please enter rock, paper, or scissors:")
    userChoice = input()

#Random code function (The code for the computer picking random r p s)
import random

#List of choices
choices = ['rock', 'paper', 'scissors']

#computer choice
computerChoice = random.choice(choices)

#response to the "which will you choose?" question
print(f"I chose: {computerChoice}")

#Code for if user won or computer won.
def determineWinner(user, computer):
    if user == computer:
        return "I guess we tied!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "Ah shucks, you won!"
    else:
        return "Yippee! I won!"

# Determine the result and print it
result = determineWinner(userChoice, computerChoice)
print(f"{result}")