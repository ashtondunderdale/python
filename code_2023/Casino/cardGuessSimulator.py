import random

def playCardGuessGame():
    """starts a card guessing game, user can guess either colour, number, or specific card"""

    deck = ["Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades",
            
            "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts",
            
            "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds",

            "Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs"]

    # picks a random card from the deck
    card = random.choice(deck)
    card = card.lower()
    print(f"A card has been drawn from the deck {card}")
    choice = input("Would you like to guess the colour, number, or card specifically?\n\n1. suit\n2. value\n3. card\n")

    if choice == "1":   
        # asks the user to guess the colour of the card
        colorGuess = input("Enter your guess for the color of the card (red or black): ")

        if colorGuess.lower() == "hearts" and card.endswith("hearts"):
            print(f"Correct, the card was: {card}")

        elif colorGuess.lower() == "spades" and card.endswith("spades"):
            print(f"Correct, the card was: {card}")

        elif colorGuess.lower() == "clubs" and card.endswith("clubs"):
            print(f"Correct, the card was: {card}")

        elif colorGuess.lower() == "diamonds" and card.endswith("diamonds"):
            print(f"Correct, the card was: {card}")

        else:
            print(f"Incorrect, the card was: {card}")
            
    elif choice == "2":
        # asks the user to guess for what number the card is 
        numberGuess = input("Enter your guess for the value of the card: ")

        if numberGuess in card:
            print(f"Correct, the card was: {card}")
        else:
            print(f"Incorrect, the card was: {card}")
                    
    elif choice == "3":
        # asks the user to guess what card specifically it is
        specificGuess = input("Enter your guess for the specific card: ")

        if specificGuess == card:
            print(f"Correct, the card was: {card}")
        else:
            print(f"Incorrect, the card was: {card}")

playCardGuessGame()