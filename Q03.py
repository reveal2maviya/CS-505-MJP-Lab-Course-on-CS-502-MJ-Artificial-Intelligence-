"""
Program: Set Operations
Description: This program demonstrates various set operations in Python.

Set Operations:
1. Union
2. Intersection
3. Difference
4. Symmetric Difference

How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 set_operations.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python set_operations.py" to run the program.
"""

# Set Operations Program

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# 1. Union of two sets
union_set = set1 | set2

# 2. Intersection of two sets
intersection_set = set1 & set2

# 3. Difference between two sets
difference_set = set1 - set2

# 4. Symmetric Difference of two sets
symmetric_difference_set = set1 ^ set2

# Print the results
print("Set 1:", set1)
print("Set 2:", set2)
print("Union Set:", union_set)
print("Intersection Set:", intersection_set)
print("Difference Set:", difference_set)
print("Symmetric Difference Set:", symmetric_difference_set)
