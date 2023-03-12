import re

def validateEmail(email):
  """validates a given email address"""

  pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

  # checks if pattern is equal to email given
  if re.match(pattern, email):
    return True
  else:
    return False

print(validateEmail("example@gmail.com"))  