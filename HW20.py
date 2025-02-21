#Name:Ryan Pool
#Class: 6th Hour
#Assignment: HW20


#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.

try:
    print(x)
except:
    print("Hello World!")


#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.

userInt = int(input("Please enter a number: "))

try:
    print(100/userInt)
except ZeroDivisionError:
    print("Cannot be divided by 100.")

#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.

try:
    k = int(input("Please choose a second number: "))
    print(k)
except ValueError:
    print("Value not an Integer.")

#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.

i = 5
while i >= 0:
    print(i)
    i -= 1
    if i < 0:
        raise Exception("Sorry, no numbers below zero.")