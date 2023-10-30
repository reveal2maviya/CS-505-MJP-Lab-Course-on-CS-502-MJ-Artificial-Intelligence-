# Question (c): Program to find the factorial of the given number

# Get the number for which the factorial should be calculated
num = int(input("Enter a number: "))

# Initialize the factorial to 1
factorial = 1

# Calculate the factorial
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")