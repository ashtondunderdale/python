numberOne, numberTwo = int(input("Enter a number")), int(input("Enter another number"))

operation = input("Enter the operation you want to use")

if operation == "+":
    print(numberOne, "+", numberTwo, "=", numberOne + numberTwo)

elif operation == "-":
    print(numberOne, "-", numberTwo, "=", numberOne - numberTwo)

elif operation == "*":
    print(numberOne, "*", numberTwo, "=", numberOne * numberTwo)

elif operation == "/":
    print(numberOne, "/", numberTwo, "=", numberOne / numberTwo)