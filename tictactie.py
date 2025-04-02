def print_board(board):
    """Print the Tic Tac Toe board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    """Check if the given player has won."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    """Check if the board is full (no more moves possible)."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    # Initialize the empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0  # Player X starts

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn.")

        # Get the player's move
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Cell already taken. Choose another one.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as 0, 1, or 2.")

        # Print the updated board
        print_board(board)

        # Check for a winner
        if check_winner(board, player):
            print(f"Player {player} wins!")
            break

        # Check for a draw
        if is_full(board):
            print("It's a draw!")
            break

        # Switch turns
        turn += 1

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
