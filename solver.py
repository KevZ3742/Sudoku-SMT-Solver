from z3 import *

def SudokuSolver(puzzle):
    size = 9
    board = [[Int("cell_%s_%s" % (i, j)) for j in range(size)] for i in range(size)]

    constraints = [If(puzzle[i][j] != 0, board[i][j] == puzzle[i][j], True) for i in range(size) for j in range(size)]
    cells = [And(1 <= board[i][j], board[i][j] <= size) for i in range(size) for j in range(size)]
    rows = [Distinct(board[i]) for i in range(size)]
    cols = [Distinct([board[i][j] for i in range(size)]) for j in range(size)]
    subarrays = [Distinct([board[i + k][j + l] for k in range(3) for l in range(3)]) for i in range(0, 9, 3) for j in range(0, 9, 3)]
    constraints = constraints + cells + rows + cols + subarrays

    s = Solver()
    s.add(constraints)

    if s.check() == sat:
        m = s.model()
        solution = [[m.evaluate(board[i][j]).as_long() for j in range(size)] for i in range(size)]
        return solution
    else:
        return "unsat"