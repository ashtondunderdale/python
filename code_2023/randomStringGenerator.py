import random
import string

# all parameter inputs from user - sets whether certain characters will be included in the generated sequence
uppercaseCharacters = input("Include uppercase characters (y/n)? ").lower() == "y"
lowercaseCharacters = input("Include lowercase characters (y/n)? ").lower() == "y"
digits = input("Include digits (y/n)? ").lower() == "y"
specialCharacters = input("Include special characters (y/n)? ").lower() == "y"
sequenceLength = int(input("Enter the length of the sequence: "))


def generateSequence(uppercaseCharacters, lowercaseCharacters, digits, specialCharacters, sequenceLength):
  """checks if parameters are "true" and adds to a list: "characters", outputs sequence based on length and cases"""

# sets characters to empty string, checks if char type is "true": uppercase, lowercase, etc
  characters = ""
  if uppercaseCharacters:
    characters = characters + string.ascii_uppercase  
  if lowercaseCharacters:
    characters = characters + string.ascii_lowercase
  if digits:
    characters = characters + string.digits
  if specialCharacters:
    characters = characters + string.punctuation

# creates var: "sequence", adds random chars from characters in accordance with length
  sequence = "".join(random.choices(characters, k=sequenceLength)) 
  
  return sequence

print(generateSequence(uppercaseCharacters, lowercaseCharacters, digits, specialCharacters, sequenceLength))

