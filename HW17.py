#Name: Ryan Pool
#Class: 6th Hour
#Assignment: HW17


#1. Import the "random" library and create a def function that prints "Hello World!"

import random

def helloWorld():
    print("Hello World")

#2. Create two empty integer variables named "heads" and "tails"

heads = 0
tails = 0

#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.

def coinFlip():
    global heads
    global tails

    for i in range(100):
        result = random.choice(['heads', 'tails'])
        if result == 'tails':
            tails += 1
        else:
            heads += 1


#4. Call the "Hello world" and "Coin Flip" functions here

helloWorld()
coinFlip()

#5. Print the final result of heads and tails here

print("heads count:", heads, "tails count:", tails)