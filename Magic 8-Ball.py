#Ryan Pool
#9.10.24

#Make computer respond to user with random magic 8-ball responses.

#Conversation between user and computer leading up to the 8-ball
userName = input("Please enter your name before we proceed: ")
print("Hello", userName, "I shall answer your most dearest questions")

#Input for user to ask a question
userQuestion = input("What is your question: ")

#Conversation leading up to answer
print("Ah quite the question. Let me consult the elders...")

#List of 8-ball responses
responseList = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it"]
responseList2 = ["As I see is, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again"]
responseList3 = ["Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"]
responseList4 = ["Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

#Combining all lists into 1 list
allLists = [responseList, responseList2, responseList3, responseList4]

#Random code function
import random

#Randomly choosing one list
chosenList = random.choice(allLists)

#Computer random choice from chosen list
chosenSentence = random.choice(chosenList)

#Actual response with 8-ball wisdom
print(f"{chosenSentence}")
