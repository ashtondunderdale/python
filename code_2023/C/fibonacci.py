def fibonacciSequence(num):
    """prints the fibonacci sequence up to a given number"""

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacciSequence(num-1) + fibonacciSequence(num-2)

term = int(input("Enter the number of terms in the Fibonacci sequence: "))

for i in range(term):
    print(fibonacciSequence(i))