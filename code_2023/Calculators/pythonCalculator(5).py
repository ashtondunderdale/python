def calculator(numberOne, numberTwo, operation):
    """simple calculator for python"""

    if operation == "+":
        print(numberOne, "+", numberTwo, "=", numberOne + numberTwo)

    elif operation == "-":
        print(numberOne, "-", numberTwo, "=", numberOne - numberTwo)

    elif operation == "*":
        print(numberOne, "*", numberTwo, "=", numberOne * numberTwo)

    elif operation == "/":
        print(numberOne, "/", numberTwo, "=", numberOne / numberTwo)
    exit()

def getNumbers():
    """gets the input values from the user"""

    numberOne, numberTwo = input("Enter a number"), input("Enter another number")
    
    if not numberOne.isdigit() or not numberTwo.isdigit():
        print("Error: One or both of the provided numbers are not a valid number")
        getNumbers()
    
    numberOne, numberTwo = int(numberOne), int(numberTwo)
    operation = input("Enter the operation you want to use")
    

    if operation not in ["+", "-", "*", "/"]:
        print("Error: Unsupported operation")
        getNumbers()
    
    calculator(numberOne, numberTwo, operation)

    return numberOne, numberTwo, operation

numberOne, numberTwo, operation = getNumbers()
