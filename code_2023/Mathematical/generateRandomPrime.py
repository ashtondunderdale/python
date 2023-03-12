import random

def checkPrime(num):
    """Checks if a number is prime"""

    if num <=1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generatePrime():
    """Generates a random number"""
    
    while True:
        num = random.randint(1, 100)
        if checkPrime(num):
            return num
        
primeNumber = generatePrime()
print("Prime Number:", primeNumber)