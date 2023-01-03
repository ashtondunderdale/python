import random

def playDiceSimulator():
    """simulates a guessing game of what side the dice will land on"""

    # sets up the loop for playing again
    playing = True
    while playing:

        guess = input("Enter what side you think it will land on: ") 
        dice = random.randint(1, 6)

        # checks if the dice is equal to guess
        if guess == str(dice):
            print(f"The roll was {dice}, you guessed {guess}, You Win!")
        else: 
            print(f"The roll was {dice}, you guessed {guess}, You Lose!")

        # asks the user if they want to play again
        playAgain = input("Do you want to play again? (y/n)")
        if playAgain.lower() == "n":
            playing = False

playDiceSimulator()