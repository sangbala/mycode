#!/usr/bin/env python3

round=0
answer=" "

while True:
    
    round=round+1 # increase the round counter by 1
    print('Finish the movie title, "Monty Python\'s The Life of ..."')

    answer=input("Your guess--> ")
    answer=answer.upper()
    
    if answer=="SHRUBBERY":
        print("You gave the super secret answer!")
        break

    elif answer=="BRIAN":  # logic to check if user gave correct answer
        print('Correct')
        break

    elif round==3:   # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
        break

    else: # if answer was wrong
        print("Sorry! Try again!")

