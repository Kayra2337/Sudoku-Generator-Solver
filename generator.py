import numpy as np
from utils import is_valid, find_empty
from solver import count_solutions

def fill_board(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    numbers = list(range(1, 10))
    np.random.shuffle(numbers)
    for num in numbers:
        if is_valid(board, row, col, num):
            board[row, col] = num
            if fill_board(board):
                return True
            board[row, col] = 0
    return False

def generate_full_board():
    board = np.zeros((9, 9), dtype=int)
    fill_board(board)
    return board

def make_puzzle(board, max_removed=40):
    puzzle = board.copy()
    cells = [(i, j) for i in range(9) for j in range(9)]
    np.random.shuffle(cells)
    removed = 0
    for row, col in cells:
        temp = puzzle[row, col]
        puzzle[row, col] = 0
        board_copy = puzzle.copy()
        if count_solutions(board_copy) != 1:
            puzzle[row, col] = temp
        else:
            removed += 1
        if removed >= max_removed:
            break
    return puzzle

# 🔧 Eksik olan fonksiyon
def generate_sudoku(max_removed=40):
    full_board = generate_full_board()
    puzzle = make_puzzle(full_board, max_removed=max_removed)
    return puzzle
