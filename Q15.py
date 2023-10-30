"""
Program: Tic-Tac-Toe Game
Description: This program allows two players to play a game of Tic-Tac-Toe in the terminal.
How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 tic_tac_toe.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python tic_tac_toe.py" to run the program.
"""

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):  # Check diagonals
        return True
    return False

# Function to check if the board is full (a draw)
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Main function to play the Tic-Tac-Toe game
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    win = False

    print("Tic-Tac-Toe Game:")
    print_board(board)

    while not win and not check_draw(board):
        print(f"Player {player}, enter your move (row and column):")
        row, col = map(int, input().split())

        if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = player
            win = check_win(board, player)
            player = "O" if player == "X" else "X"
            print_board(board)
        else:
            print("Invalid move. Try again.")

    if win:
        print(f"Player {player} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
