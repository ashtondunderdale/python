import random

suits = ["hearts", "diamonds", "spades", "clubs"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

numberOfCards = int(input("Enter the number of cards to generate: "))


def generateCard(suits, ranks):
  """generates a random suit and rank"""

  suit = random.choice(suits)
  rank = random.choice(ranks)

  return f"{rank} of {suit}"

# calls the function "generateCard" for the user specified amount, outputs card(s)"
for i in range(numberOfCards):
  card = generateCard(suits, ranks)
  print(card)