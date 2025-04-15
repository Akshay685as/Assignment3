# Task 5: Calculate Factorial Using a Function

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking input from user
number = int(input("Enter a number: "))

# Calculating factorial
fact = factorial(number)

# Displaying result
print(f"Factorial of {number} is: {fact}")