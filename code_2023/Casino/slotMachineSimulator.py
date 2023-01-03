import random

symbols = ["seven", "diamond", "cherry"]
prizes = [100, 50, 10]


def spin():
    """generates 3 slot machine symbols, returns as list"""

    symbol1 = random.choice(symbols)
    symbol2 = random.choice(symbols)
    symbol3 = random.choice(symbols)

    return [symbol1, symbol2, symbol3]


def getPrizeAmount(symbols, prizes):
    """gets the index of the winning symbol and allocated prize for the symbol index"""

    index = symbols.index(result[0])

    return prizes[index]

# set up the loop to continue until the user decides to stop playing
playing = True
while playing:
    result = spin()
    print(result)

    # checks if symbols are same, gets prize for that match, outputs winnings
    if result[0] == result[1] == result[2]:
        prize = getPrizeAmount(symbols, prizes)
        print(f"You won ${prize}! You got three {result[0]}s in a row")
    else:
        print("No Match")

    # asks the user if they want to play again
    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() == "n":
        playing = False