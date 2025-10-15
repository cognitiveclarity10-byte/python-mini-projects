import random   # Random module produces random integer numbers 


# randint will assign a random number in between 1 to 100 
# to the randomNubmer variable 
randomNumber = random.randint(1,10)

# A while loop is used to run the code until the corect number is found 

count = 5
while count != 0:
    # The try and except is used if the user typed an not integer input 
    try:
        askUserNumber = int(input("Guess a Number from 1 to 100 : "))
        """The number gussed by the user is checked if it is higher or lower than the
        random number generated  when the user get the correct number it exit the loop """
        if askUserNumber < randomNumber:
            print("Guess Higher")
            print()
        elif askUserNumber > randomNumber:
            print("Guess Lower")
            print()
        else:
            print("You got it Right !!!!")
            print()
            break 
        count -= 1
        if count != 0:
            print("You Have " + str(count) + " more chances")
            print()
        else :
            print("oh you lose")
            break
        
    except ValueError:
        print("Please enter only Numbers")
        
