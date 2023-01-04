import re

def checkStrength(password):
  """checks the strength of a password"""

  if len(password) < 8:
    return "Weak"

  if len(password) > 13:
    return "Strong"

  if not re.search(r'[a-z]', password):
    return "Weak"

  if not re.search(r'[A-Z]', password):
    return "Weak"

  if not re.search(r'\d', password):
    return "Weak"

  if not re.search(r'[^a-zA-Z\d]', password):
    return "Weak"

  return "Strong"

print(checkStrength("password"))
