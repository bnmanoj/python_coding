def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid(board, row, col, num):
    # Check if 'num' is already present in the current row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if 'num' is present in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find the first empty cell in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_location = find_empty_location(board)

    if not empty_location:
        return True  # All cells are filled, the Sudoku is solved

    row, col = empty_location

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # Continue solving recursively

            # If placing 'num' at the current location doesn't lead to a solution, backtrack
            board[row][col] = 0

    return False  # No solution found for the current configuration

if __name__ == "__main__":
    # Example Sudoku board (0 represents empty cells)
    sudoku_board = [
        [6, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [5, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 3, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku Puzzle:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSudoku Solution:")
        print_board(sudoku_board)
    else:
        print("\nNo solution exists.")
