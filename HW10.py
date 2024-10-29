#Name: Ryan Pool
#Class: 6th Hour
#Assignment: HW10

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    i -= 1
else:
    print("Hello World")

#2. Create a while loop that prints only even numbers
#between 1 and 30.
n = 0
while n <= 30:
    if n % 2 == 0:
        print(n)
        n += 2
else:
    print("Hello World")

#3. Create a while loop that repeats until the user
#inputs the number 0.

p = int(input('Enter a number: '))
while p != 0:
    print(p)
    p = int(input('Enter a number: '))

