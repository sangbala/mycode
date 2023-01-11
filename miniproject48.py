#!/usr/bin/python3
import random
#explain what we are going to do
print("Guess what number I'm thinking of! [0,100]. You have 10 times to try.")

#generate the number I am thinking of
theNumber=random.randint(0, 100)
#print(theNumber)

count=0

while True and count <= 11:

    #keep track of how many times user has tried
    count += 1
    if count == 11:
        print("You have tried 10 times.")
        break

    #there may be error from input
    try:

        #prompt user to put in a number
        yourGuess = int(input("What number do you think?"))
        if yourGuess == theNumber:
            print("You got it. The number is "+str(theNumber))
            break
        elif yourGuess < theNumber:
            print("Hint: The number is larger than your input.")
            print("Please try a number larger than " + str(yourGuess))
        else:
            print("Hint: The number is smaller than your input.")
            print("Please try a number smaller than " + str(yourGuess))

    #catch the value error
    except ValueError as verr:

        print("Handling value error:", verr)

    # general error handling
    except Exception as err:
        print("We did not anticipate that:", err)
