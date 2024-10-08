#Name: Ryan Pool
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World")

#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = True
admin = False

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
adminLoginCount = 0

#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi:
    if login:
        if admin:
            print("Welcome!")
            adminLoginCount += 1
        else:
            print("Error no admin access")
    else:
        print("Error no login")
else:
    print("Error no wifi connection")

print(f"Admin login count: {adminLoginCount}")

