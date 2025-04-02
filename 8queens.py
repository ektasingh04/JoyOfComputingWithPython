def print_board(board):
    """Function to print the chessboard"""
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


def is_safe(board, row, col):
    """Check if it's safe to place a queen at position (row, col)"""
    # Check the column
    for i in range(row):
        if board[i][col]:
            return False


    # Check the diagonal (top-left to bottom-right)
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False


    # Check the diagonal (top-right to bottom-left)
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i][j]:
            return False


    return True


def solve_n_queens(board, row):
    """Use backtracking to solve the N-Queens problem"""
    n = len(board)

    # If all queens are placed, return True (solution found)
    if row >= n:
        return True

    # Try placing the queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = True  # Place the queen

            # Recur to place the next queen
            if solve_n_queens(board, row + 1):
                return True

            # If placing queen leads to no solution, backtrack
            board[row][col] = False

    # If no place is found, return False
    return False


def solve():
    n = 8  # Size of the chessboard (8x8 for the 8 queens problem)
    board = [[False for _ in range(n)] for _ in range(n)]  # Initialize the chessboard


    if solve_n_queens(board, 0):  # Start solving from the first row
        print_board(board)
    else:
        print("No solution found")


# Run the solver
solve()
