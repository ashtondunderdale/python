def fibonacci(n):
    """prints the fibonacci sequence up to a given number"""

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

for i in range(terms):
    print(fibonacci(i))