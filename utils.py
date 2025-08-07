# sudoku_utils.py
import numpy as np

def is_valid(board, row, col, num):
    if num in board[row] or num in board[:, col]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row+3, start_col:start_col+3]:
        return False
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i, j] == 0:
                return i, j
    return None
