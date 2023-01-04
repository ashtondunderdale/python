import random

def getUserPrediction():
  """gets user prediction for heads or tails"""

  while True:
    prediction = input("Enter your prediction (heads or tails): ").lower()
    if prediction in ['heads', 'tails']:
      return prediction
    print("Invalid input. Please enter 'heads' or 'tails'.")


def playCoinFlip():
  """plays a game of coin flip and returns the result"""

  result = random.choice(['heads', 'tails'])
  prediction = getUserPrediction()

  print("The coin flip was", result)

  # checks if prediction was correct, outputs accordingly
  if prediction == result:
    print("Correct!")
    return "correct"
  else:
    print("Incorrect!")
    return "incorrect"


def main():
  """asks the user if they want to play again, outputs right / wrong predictions"""

  counts = {"correct": 0, "incorrect": 0}

  # starts the coinflip process with the function "playCoinFlip" 
  while True:

    result = playCoinFlip()
    # counter for correct and incorrect guesses
    counts[result] += 1

    # asks the user if they would like to play again
    while True:
      flipAgain = input("Would you like to play again (y/n)? ").lower()
      if flipAgain in ["y", "n"]:
        break
      print("Invalid input. Please enter 'y' or 'n'.")

    if flipAgain != "y":
      break

  print("Correct:", counts["correct"])
  print("Incorrect:", counts["incorrect"])

main()