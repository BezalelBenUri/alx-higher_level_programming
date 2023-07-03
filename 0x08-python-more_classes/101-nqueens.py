#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position (row, col) on the board.
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    """
    Solve the N-queens problem using backtracking.
    """
    # Base case: all queens are placed
    if col >= N:
        print_solution(board)
        return True

    # Recur for each row in the current column
    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen on the board
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_n_queens(board, col + 1)

            # Backtrack and remove the queen from the board
            board[i][col] = 0

    return False

def print_solution(board):
    """
    Print the solution as a list of queen positions.
    """
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

# Check the number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check the value of N
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty board
board = [[0 for _ in range(N)] for _ in range(N)]

# Solve the N-queens problem
solve_n_queens(board, 0)
