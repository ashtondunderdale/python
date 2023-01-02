import re

def validateEmail(email):
  pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
  if re.match(pattern, email):
    return True
  else:
    return False

print(validateEmail("example@gmail.com"))  

