import random

slotSymbols = ["cherry", "lemon", "orange", "plum", "bell", "bar"]

def spinSlots():
  symbol1 = random.choice(slotSymbols)
  symbol2 = random.choice(slotSymbols)
  symbol3 = random.choice(slotSymbols)

  return [symbol1, symbol2, symbol3]

result = spinSlots()

print(result)