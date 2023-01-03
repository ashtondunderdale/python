import random

while True:

    outcomes = ["10", "10", "10", "10", "10", "10", "10", "10",
    "No Win", "No Win", "No Win", "No Win", "No Win","No Win", "No Win", "No Win", "No Win", "No Win", 
    "No Win", "No Win", "No Win", "No Win", "No Win", "No Win", "No Win", "No Win","No Win", "No Win"
    "25", "25", "25", "25", "50", "50", "100", "100", "250", "250", "500", "1000"]

    # generates result and checks if user has won / lost
    result = random.choice(outcomes)
    if result == "No Win":
        print("You Lost!")
    else:
        print("You spun:", result)

    # asks the player if they want to play again
    play_again = input("Do you want to spin again? (y/n) ")
    if play_again.lower() != "y":
        break