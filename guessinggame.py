#Stephen Delacalzada-Delong
#CIS 261
#Week 2 - Lab: Guessing Game

import random

#init vars
continuePlay = "y"

#Display heading
def displayHeading():
    print(f"Guess the Number!\n")

def play(limitNum):
    tryCount = 0
    print(f"I'm thinking of a number from 1 to {limitNum}\n")
    randomNum = random.randint(1, limitNum)
    guessNum = int(input("Your guess: "))
    while(guessNum != randomNum):
        if guessNum<randomNum:
            print("Too low.")
            tryCount += 1
        elif guessNum>randomNum:
            print("Too high.")
            tryCount += 1
        guessNum = int(input("Your guess: "))
    print(f"You guessed it in {tryCount}")



#entry point
def main():
    displayHeading()
    global continuePlay

    while continuePlay.lower() == "y":
        limitNum = int(input("Enter the limit: "))
        play(limitNum)
        continuePlay = input(f"Would you like to play again? (y/n): \n")
    print("Bye!")

if __name__ == "__main__":
    main() 