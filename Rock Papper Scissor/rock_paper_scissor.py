import random 

# Giving information to the User
print("Enter\n R for Rock\n P for Paper\n S for Scissor\n")


# This function used for the computer  to pick a random number and 
# check it against the user choice 
def rock_paper_scissor():

    computerChoice = random.randint(1,3)
    userInput = input("Enter R/P/S : ").lower()

    if computerChoice == 1:
        print("Rock")
        if userInput == "r":
            print("It is a Draw") 
        elif userInput == "s":
            print("Oh no YOU LOSE!!!!!")
        elif userInput == "p":
            print("Yeahhh You Win")
        else:
            print("Invalid Input")

    elif computerChoice == 2:
        print("Paper")
        if userInput == "r":
            print("Oh no YOU LOSE!!!!!") 
        elif userInput == "p":
            print("It is a Draw")
        elif userInput == "s":
            print("Yeahh You Win !!!")
        else:
            print("Invalid Input")
    
    elif computerChoice == 3:
        print("Scissor")
        if userInput == "s":
            print("It is a Draw") 
        elif userInput == "p":
            print("Oh no YOU LOSE!!!!!")
        elif userInput == "r":
            print("Yeahh You Win !!!")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")



# loop runs until the user says no  in the loop another if is used to check the 
# the user wants to play or not 
def main():
    while True:
    
        ask = input("Do you want to play Rock Paper Scissor Yes/No : ").lower()
        
        

        if ask == "yes":
            rock_paper_scissor()
        elif ask == "no":
            print("See you Again")
            break
        else:
            print("Please Only Enter Yes/No")



if __name__ == "__main__":
    main()

    
