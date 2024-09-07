#Ryan Pool
#Playground
#6th Hour

#The conversation between user and computer leading up to the game
userName = input("What is your name? ")
print("Hello",userName)
input("Would you like to play Rock, Paper, Scissors? ")

#Asking which will user choose?
userChoice = input("You'll play anyway. So, Rock Paper or Scissors? ").lower()

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