# Question (a): Program to print a multiplication table for a given number

# Get the number for which the multiplication table should be printed
num = int(input("Enter a number: "))

# Print the multiplication table for the given number (up to 10)
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
