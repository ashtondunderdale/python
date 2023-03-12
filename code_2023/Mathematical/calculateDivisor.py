def calculateGreatestCommonDivisor(a, b):
    """calculates the greatest common divisor of two numbers"""

    if b == 0:
        return a     
    else:
        return calculateGreatestCommonDivisor(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The GCD of", num1, "and", num2, "is", calculateGreatestCommonDivisor(num1, num2))
