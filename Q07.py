"""
Program: Water Jug Problem
Description: This program solves the Water Jug Problem, where you have two jugs of different capacities and need to measure a specific amount of water.

How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 water_jug_problem.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python water_jug_problem.py" to run the program.
"""

# Function to perform water jug operations and find a solution
def water_jug_problem(capacity_x, capacity_y, target):
    jug_x = 0
    jug_y = 0

    while jug_x != target and jug_y != target:
        print(f"Jug X: {jug_x}L, Jug Y: {jug_y}L")

        # Fill jug X if it is empty
        if jug_x == 0:
            jug_x = capacity_x
            print("Fill Jug X")

        # Transfer water from jug X to jug Y if jug X is not empty
        elif jug_x > 0 and jug_y < capacity_y:
            transfer = min(jug_x, capacity_y - jug_y)
            jug_x -= transfer
            jug_y += transfer
            print("Transfer from Jug X to Jug Y")

        # Empty jug Y if it is full
        elif jug_y == capacity_y:
            jug_y = 0
            print("Empty Jug Y")

    print(f"Jug X: {jug_x}L, Jug Y: {jug_y}L")
    print("Solution Found!")

# Main function to initiate the problem
def main():
    capacity_x = 4  # Capacity of jug X
    capacity_y = 3  # Capacity of jug Y
    target = 2     # Amount of water to measure

    print("Solving Water Jug Problem:")
    water_jug_problem(capacity_x, capacity_y, target)

if __name__ == '__main__':
    main()
