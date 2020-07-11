"""
Use backtracking algorithm to solve Sudoku puzzle.

General backtracking pseudo-code from CS50's AI series.

function backtrack(assignment, constraintProblem):
    if assignment complete: return assignment
    var = selectUnassignedVar(assignment, constraintProblem)
    for value in DOMAIN_VALUES(var, assignment, constraintProblem):
        if value consistent with assignment:
            add {var = value} to assignment
            result = backtrack(assignment, constraintProblem)
            if result != failure: return result
        remove {var = value} from assignment
    return failure
"""

board = [[1,-1,3,2],
        [-1,-1,1,4],
        [4,1,2,-1],
        [2,3,-1,-1]]
for row in board:
    print(row)
