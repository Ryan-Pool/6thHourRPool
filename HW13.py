#Name: Ryan Pool
#Class: 6th Hour
#Assignment: HW13


#1. Create a list containing 10 integers of your choice.
list = [3, 7, 2, 1, 6, 7, 9, 10, 11, 54]

#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0

#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
#for i in list:

for num in list:
    if num % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1

# Print the total count of even and odd numbers.

print("The amount of even numbers are: ", evenNumbers)

print("The amount of odd numbers are: ", oddNumbers)