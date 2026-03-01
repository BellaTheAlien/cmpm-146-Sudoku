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

# Example usage
sudoku_board = generate_sudoku_board()
for row in sudoku_board:
    print(row)
