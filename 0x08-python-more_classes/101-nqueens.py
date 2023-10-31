#!/usr/bin/python3

import sys

def placeNQueens(board, r):
    comp_len = len(board)
    if r == comp_len:
        print([[y for y in x] for x in board])
        return
    for i in range(comp_len):
        if noKill(board, r, i):
            board[r] = ["." * i + "Q" + "." * (comp_len - i - 1)]
            placeNQueens(board, r + 1)
            

def noKill(board, ocuppied_rows, o_cols):
    for i in range(ocuppied_rows):
        if "Q" in board[i][0][o_cols]:
            return False
        if o_cols + ocuppied_rows - i < len(board) and "Q" in board[i][0][o_cols + ocuppied_rows - i]:
            return False
        if o_cols - ocuppied_rows + i >= 0 and "Q" in board[i][0][o_cols - ocuppied_rows + i]:
            return False
    return True


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [["." * N] for _ in range(N)]
placeNQueens(board, 0)
