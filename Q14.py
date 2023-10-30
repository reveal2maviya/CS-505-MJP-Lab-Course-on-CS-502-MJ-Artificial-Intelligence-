"""
Program: N-Queens Puzzle using Forward Checking
Description: This program solves the N-Queens puzzle using forward checking.
How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 nqueens.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python nqueens.py" to run the program.
"""

# Function to print the chessboard with queens
def print_chessboard(chessboard):
    for row in chessboard:
        print(" ".join(row))

# Function to check if it's safe to place a queen at the given position
def is_safe(chessboard, row, col, n):
    # Check the column
    for i in range(row):
        if chessboard[i][col] == 'Q':
            return False

    # Check the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if chessboard[i][j] == 'Q':
            return False

    # Check the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if chessboard[i][j] == 'Q':
            return False

    return True

# Recursive function to solve the N-Queens problem using forward checking
def solve_nqueens(chessboard, row, n):
    if row >= n:
        return True  # All queens are placed

    for col in range(n):
        if is_safe(chessboard, row, col, n):
            chessboard[row][col] = 'Q'  # Place a queen

            if solve_nqueens(chessboard, row + 1, n):
                return True

            chessboard[row][col] = '.'  # If placing a queen doesn't lead to a solution, backtrack

    return False  # No solution exists

# Main function to perform N-Queens puzzle with forward checking
def main():
    n = 8  # Size of the chessboard (8x8)
    chessboard = [['.' for _ in range(n)] for _ in range(n)]

    print("N-Queens Puzzle using Forward Checking:")
    if solve_nqueens(chessboard, 0, n):
        print("\nSolution to the N-Queens Puzzle:")
        print_chessboard(chessboard)
    else:
        print("No solution found.")

if __name__ == '__main__':
    main()
