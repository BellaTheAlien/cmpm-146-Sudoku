# the start of a basic sudoku bord generator

import random

def generate_sudoku_board():
    # Create an empty 9x9 board
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Fill the diagonal 3x3 boxes
    for i in range(0, 9, 3):
        fill_box(board, i, i)

    # Fill the remaining cells
    # this is a backtracking algorithm to solve the sudoku board (we don't need but nice to have)
    # fill_remaining_cells(board) 

    return board

# keep this function, this is the one that generates random numbers in the board
def fill_box(board, row_start, col_start):
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for i in range(3):
        for j in range(3):
            board[row_start + i][col_start + j] = numbers[i * 3 + j]

def fill_remaining_cells(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_safe(board, i, j, num):
                        board[i][j] = num
                        if fill_remaining_cells(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def is_safe(board, row, col, num):
    # Check if 'num' is not in the given row and column
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    # Check if 'num' is not in the 3x3 box
    box_row_start = row - row % 3
    box_col_start = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[box_row_start + i][box_col_start + j] == num:
                return False

    return True

# adding the playable element to the board
def print_board(board):
    print("\n   0 1 2    3 4 5    6 7 8")
    print("  +-------+-------+-------+")

    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("  +-------+-------+-------+")
        
        row_start = f"{i} |"
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_start += " |"
            row_start += (str(val) if val != 0 else ".") + " "
        print(row_start)
    print("  +-------+-------+-------+")

def play_game():
    board = generate_sudoku_board()

    while True:
        print_board(board)
        print("Enter your move (row col number) or 'q' to quit:")

        user_input = input("> ").strip().lower()

        if user_input == 'q':
            print("Thanks for playing!")
            break

        try:
            row, col, num = map(int, user_input.split())

            if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                print("Invalid input.")
                continue

            if is_safe(board, row, col, num):
                board[row][col] = num
                print(f"Move accepted: {num} placed at ({row}, {col})")
            else:
                print(f"Move rejected: {num} cannot be placed at ({row}, {col})")
        except ValueError:
            print("Invalid input format. Please enter row, column, and number separated by spaces.")

if __name__ == "__main__":
    play_game()
