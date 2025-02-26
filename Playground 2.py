# Random code function (The code for the computer picking random r p s)
import random

# List of choices
choices = ['rock', 'paper', 'scissors']

# Computer choice
computerChoice = random.choice(choices)

# The conversation between you and the computer leading up to the game
userName = input("What is your name? ")
print("Hello", userName)

#Computer asking if user wants to play r p s
userResponse = input("Would you like to play Rock, Paper, Scissors? ")

#Add code for if user inputs no or yes
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

# Asking which will you choose? Uses try except to throw up error if user does not enter from choices.
userChoice = input()

if not type(userChoice) is choices:
    raise Exception("Sorry, you can only enter rock, paper, or scissors.")
else:
# Response to the "which will you choose?" question
    print(f"I chose: {computerChoice}")

# Code for if the user won or the computer won.
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
