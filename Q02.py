"""
Program: List Operations and Methods
Description: This program demonstrates various list operations and methods in Python.

List Operations:
1. Nested list
2. Length of a list
3. Concatenation of two lists
4. Membership testing
5. Iteration over a list
6. Indexing and Slicing

List Methods:
7. Add an element to the end of the list
8. Extend the list with another list
9. Delete an element by value

How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 list_operations.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python list_operations.py" to run the program.
"""

# List Operations and Methods Program

# Create a list
my_list = [1, 2, 3, 4, 5]

# 1. Nested list
nested_list = [my_list, ['a', 'b', 'c']]

# 2. Length of a list
list_length = len(my_list)

# 3. Concatenation of two lists
concatenated_list = my_list + ['x', 'y', 'z']

# 4. Membership testing
if 3 in my_list:
    print("3 is in the list")
if 'x' not in my_list:
    print("x is not in the list")

# 5. Iteration over a list
print("Iterating over my_list:")
for item in my_list:
    print(item)

# 6. Indexing and Slicing
first_item = my_list[0]  # Access the first item
sliced_list = my_list[1:4]  # Get a slice from index 1 to 3

# 7. List Methods

# 7.1 Add an element to the end of the list
my_list.append(6)

# 7.2 Extend the list with another list
my_list.extend([7, 8, 9])

# 7.3 Delete an element by value
my_list.remove(2)

# Print the results
print("Original List:", my_list)
print("Nested List:", nested_list)
print("Length of the List:", list_length)
print("Concatenated List:", concatenated_list)
print("First Item:", first_item)
print("Sliced List:", sliced_list)
