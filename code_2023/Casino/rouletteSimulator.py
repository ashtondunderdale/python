import random

while True:

    outcomes = [("green", 0), ("red", 1), ("black", 2), ("red", 3), ("black", 4), ("red", 5), ("black", 6), ("red", 7), ("black", 8), ("red", 9), ("black", 10), ("red", 11), ("black", 12), ("red", 13), ("black", 14), ("red", 15), ("black", 16), ("red", 17), ("black", 18), ("red", 19), ("black", 20), ("red", 21), ("black", 22), ("red", 23), ("black", 24), ("red", 25), ("black", 26), ("red", 27), ("black", 28), ("red", 29), ("black", 30), ("red", 31), ("black", 32), ("red", 33), ("black", 34), ("red", 35), ("black", 36)]

    result = random.choice(outcomes)
    guess = input("Enter your guess (red, black, green, or a number): ")

    if guess.lower() == result[0]:
        print("You win!")
    elif guess.isdigit() and int(guess) == result[1]:
        print("You win!")
    else:
        print("You lose!")

    print("The ball landed on:", result[0], "The corresponding number is:", result[1])

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        break