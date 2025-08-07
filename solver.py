# sudoku_solver.py
import numpy as np
from utils import is_valid, find_empty

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row, col] = num
            if solve(board):
                return True
            board[row, col] = 0
    return False

def count_solutions(board, count=0):
    empty = find_empty(board)
    if not empty:
        return count + 1
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row, col] = num
            count = count_solutions(board, count)
            board[row, col] = 0
            if count > 1:
                break
    return count
