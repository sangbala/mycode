def main():

    # collect string input from the user
    user_input = input("Please enter your name")
    user_input1 = input("Please enter day of the weeks")
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("Hello, ", user_input, "! Happy ",user_input1)

main()
