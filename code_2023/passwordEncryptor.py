import csv
import re
import getpass
import hashlib

def setPassword(username):
  """user inputs password, validates, encrypts the password and adds to csv file"""

  with open('passwords.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if row[0] == username:
        username = input("Please enter a new username: ")
        setPassword(username)

  passwordSet = False
  while not passwordSet:
    password = getpass.getpass("Please enter a password: ")
    if not re.search("[A-Z]", password):
      print("Password must contain at least 1 capital letter")
    elif not re.search("[0-9]", password):
      print("Password must contain at least 1 number.")
    elif len(password) < 10:
      print("Password must be at least 10 characters long")
    else:
      passwordSet = True

  encryptedPassword = hashlib.sha512(password.encode()).hexdigest()

  with open('passwords.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([username, encryptedPassword])
    print("Password has been set for {}.".format(username))
    exit()

username = input("Please enter a username: ")
setPassword(username)
