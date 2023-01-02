import random


def playRockPaperScissorsRound():
  """Plays a rock paper scissors game and returns the result"""

  moves = ['rock', 'paper', 'scissors']

  while True:
    userMove = input("Enter your move (rock, paper, or scissors): ").lower()
    if userMove in moves:
      break
    print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")

  computerMove = random.choice(moves)

  if userMove == computerMove:
    print("It's a tie!")
    return "tie"
  elif (userMove == 'rock' and computerMove == 'scissors') or (userMove == 'paper' and computerMove == 'rock') or (userMove == 'scissors' and computerMove == 'paper'):
    print("You win!")
    return "user"
  else:
    print("Computer wins!")
    return "computer"


def playRockPaperScissors():
  """Plays multiple rounds of rock-paper-scissors until the user quits"""

  scores = {"user": 0, "computer": 0, "tie": 0}

  while True:
    result = playRockPaperScissorsRound()

    scores[result] += 1

    playAgain = input("Would you like to play again (y/n)? ").lower()
    if playAgain != "y":
      break

  print("\nUser Wins:", scores["user"], "\nComputer Wins:", scores["computer"], "\nTies:", scores["tie"],"\n")

playRockPaperScissors()



