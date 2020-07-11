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

# Board to solve. 0 denotes a blank or unknown value
# Starting with a simple Sudoku board as a warm up
board = [[1,0,3,2],
        [0,0,1,4],
        [4,1,2,0],
        [2,3,0,0]]

# Possible values that each element in the Sudoku board can take on
VALUES = [1,2,3,4]

# Prints the Sudoku board in a user friendly way in the output box
def printBoard(board):
    for i in range(len(board)):
        row = board[i]
        disp = ""
        for j in range(len(row)):
            item = row[j]
            disp = disp+str(item)
            # for the smaller sub boxes
            if(j == 1):
                disp = disp + "|"
            else:
                disp = disp + " "
        print(disp)
        # for the smaller sub boxes
        if(i == 1):
            print("- - - - ")

printBoard(board)
