#!/usr/bin/python3
import random


def main():
    # explain what we are going to do
    print("Guess what number I'm thinking of! [0,100]. You have 10 times to try.")

    # generate the number I am thinking of
    the_number = random.randint(0, 100)
    # print(the_number)

    count = 0

    while count <= 10:

        # keep track of how many times user has tried
        count += 1


        # there may be error from input
        try:

            # prompt user to put in a number
            your_guess = input("What number do you think?")
            if int(your_guess) == the_number:
                print("You got it. The number is " + str(the_number))
                break
            elif int(your_guess) < the_number:
                print("Hint: The number is larger than your input.")
                print("Please try a number larger than " + str(your_guess))
            else:
                print("Hint: The number is smaller than your input.")
                print("Please try a number smaller than " + str(your_guess))

        # catch the value error
        except ValueError as verr:

            print("Handling value error:", verr)

        # general error handling
        except Exception as err:
            print("We did not anticipate that:", err)

    if count == 11:
        print("You have tried 10 times.")


if __name__ == "__main__":
    main()

