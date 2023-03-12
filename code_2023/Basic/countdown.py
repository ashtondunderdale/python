import time

def countdown(n, message="Countdown Ended"):
  "starts a simple countdown function"

  while n > 0:
      print(n)
      time.sleep(1)
      n = n - 1
  print(message)

countdown(5)