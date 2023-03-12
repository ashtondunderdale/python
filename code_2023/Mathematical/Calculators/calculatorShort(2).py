def calculate():
  """calculates an expression given by the user"""

  sum = input("Enter a sum such as: 2 + 2 or 8**2\n")

  result = eval(sum)
  print("Result:", result)

calculate()


