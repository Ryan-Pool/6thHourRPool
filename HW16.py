#Name: Ryan Pool
#Class: 6th Hour
#Assignment: HW16

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
# The conversation between you and the computer leading up to the game

def game():
    userName = input("What is your name? ")
    print("Hello", userName)
    input("Would you like to play Rock, Paper, Scissors? ")

# Asking which will you choose?
    userChoice = input("You'll play anyway. So, 1 = Rock, 2 = Paper, or 3 = Scissors? ").lower()

    # Random code function (The code for the computer picking random r p s)
    import random

# List of choices
    choices = [ '1' , '2' , '3']

# Computer choice
    computerChoice = random.choice(choices)

# Response to the "which will you choose?" question
    print(f"I chose: {computerChoice}")

# Code for if the user won or the computer won.
    def determineWinner(user, computer):
        if user == computer:
            return "I guess we tied!"
        elif (user == '1' and computer == '3') or \
            (user == '3' and computer == '2') or \
            (user == '2' and computer == '1'):
            return "Ah shucks, you won!"
        else:
            return "Yippee! I won!"

# Determine the result and print it
    result = determineWinner(userChoice, computerChoice)
    print(f"{result}")

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.

    replayInput = input("Would like to play again? ")

    if replayInput == "Yes":
        game()
    else:
        exit()

game()
