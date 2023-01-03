import random

def playDiceSimulator():
    """simulates a guessing game of what side the dice will land on"""

    guess = input("Enter what side you think it will land on: ") 
    dice = random.randint(1, 6)

    # checks if the dice is equal to guess
    if guess == str(dice):
        print(f"The roll was {dice}, you guessed {guess}, You Win!")
    else: 
        print(f"The roll was {dice}, you guessed {guess}, You Lose!")

playDiceSimulator()