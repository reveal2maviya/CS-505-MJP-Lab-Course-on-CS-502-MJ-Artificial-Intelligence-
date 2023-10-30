# Question (b): Program to check whether the given number is prime or not

# Get the number to check for primality
num = int(input("Enter a number: "))

# Initialize a flag to check if the number is prime
is_prime = True

# Check if the number is less than 2
if num <= 1:
    is_prime = False
else:
    # Check if the number is divisible by any integer from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

# Determine and print the result
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
