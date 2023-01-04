def calculator():
    """simple calculator for python"""

    numberOne, numberTwo = input("Enter a number"), input("Enter another number")
    
    if not numberOne.isdigit() or not numberTwo.isdigit():
        print("Error: One or both of the provided numbers are not a valid number")
        calculator()
    
    numberOne, numberTwo = int(numberOne), int(numberTwo)
    operation = input("Enter the operation you want to use")

    if operation not in ["+", "-", "*", "/"]:
        print("Error: Unsupported operation")
        calculator()

    if operation == "+":
        print(numberOne, "+", numberTwo, "=", numberOne + numberTwo)

    elif operation == "-":
        print(numberOne, "-", numberTwo, "=", numberOne - numberTwo)

    elif operation == "*":
        print(numberOne, "*", numberTwo, "=", numberOne * numberTwo)

    elif operation == "/":
        print(numberOne, "/", numberTwo, "=", numberOne / numberTwo)
    exit()

calculator()