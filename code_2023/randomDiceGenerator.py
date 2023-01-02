import random

# gets amount of sides and rolls from user input
amountOfSides = int(input("Enter the number of sides for your dice: "))
amountOfRolls = int(input("Enter the number of times you want to roll the dice: "))

def rollDice(dice, rolls):
    """rolls the dice, generates number for dice to land on, outputs the roll number and the side it landed on"""

    for i in range(rolls):
      roll = random.randint(1, dice)
      print(f"Roll {i+1}: {roll}")

rollDice(amountOfSides, amountOfRolls)