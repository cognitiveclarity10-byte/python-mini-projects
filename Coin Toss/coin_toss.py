import random
import time, os


def coin_flip():

    flip_choice = random.randint(1,2)

    if flip_choice == 1 :
        print("Heads")
    else:
        print("Tails")



def main():

    
    while True:
        asking_user = input("Do you Want to Toss a Coin : ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')

        if asking_user =="yes":
            print("Spinning")
            time.sleep(1)
            coin_flip()
        elif asking_user =="no":
            print("Thank You for Playing")
            break
        else:
            print("Invalid Entry")




if __name__ == "__main__":
    main()


