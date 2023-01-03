def calculate(number):
    """calculates all the possible sums that can add up to a given number"""

    global result
    result = []

    # trys all the combinations
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            
            # checks if the combinations sum is equal to "number"
            if i + j == number:

                # checks its not a repeat combination ( 3 + 4, 4 + 3 )
                if i <= j:
                    result.append(f"{i} + {j}")

    print(f"There are {len(result)} different sums to make {number}")

calculate(20)
print(result)