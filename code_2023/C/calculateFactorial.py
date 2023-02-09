def calculateFactorial(n):
    """calculates the factorial of a number"""

    if n == 0:
        return 1
    else:
        return n * calculateFactorial(n-1)

num = int(input("Enter a number: "))

print("The factorial of", num, "is", calculateFactorial(num))