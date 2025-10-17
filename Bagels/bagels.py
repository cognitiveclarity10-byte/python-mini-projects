import random

print(" Welcome to Bagels \n")
print("This is a Guessing Game I will think 3 Number")
print("You Have to Guess the number\nI will give you some clues \n" \
"Pico : means the number is in correct position\n\n" \
"Farmi : means the number is there but in wrong position\n\n" \
"Bagels : the number wrong \n\n")
print()


Num_Digits = 3
Max_Guess = 3


def getNumber():

    num = random.sample(range(10),Num_Digits)
    num1 = ""

    for i in range(Num_Digits):
        num1 += str(num[i])
    num = num1
    return num

def main():
    
    
    num = 1
    
    while True:
        secretNum = getNumber()
        print(secretNum)
        while num <= Max_Guess:
            remaining = Max_Guess - num+1
            print(f"You have {remaining} more chance")
            guess = input("enter a numbre : ")
            if len(guess) != Num_Digits or not guess.isdigit():
                print("Invalid input. Try again.")
                continue
            if guess == secretNum:
                print("Yeah you got it ")
                break
            getClues(guess,secretNum)
            num +=1
        else:
            print("You are out of Guesses")
        ask = input("Do you want to play again : ").lower()
        if ask ==  "yes":
            pass
        
        else:
            
            print("thank you for playing")
            break


        


        

def getClues(guess,secretNum):    
    
    

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('pico')

        elif guess[i] in secretNum:
            clues.append('farmi')

        elif guess[i] != secretNum[i]:
            clues.append('bagels')

    print(' '.join(clues))


if __name__ == "__main__":
    main()