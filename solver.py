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


"""
Board to solve. 0 denotes a blank or unknown value.
"""
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def resetBoard(board: list):
    """
    Resets the board to its original values.

    @param board:list
        List of lists representing the Sudoku board of size 9x9.
    """
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]


def printBoard(board: list):
    """
    Prints the Sudoku board in a user friendly way in the output box.

    @param board:list
        List of lists representing the Sudoku board of size 9x9.
    """
    for i in range(len(board)):
        row = board[i]
        disp = ""
        # Displays each element in the row, adding vertical bar where necessary
        for j in range(len(row)):
            item = row[j]
            disp = disp+str(item)
            # for the smaller sub boxes
            if(j%3 == 2 and j!=8):
                disp = disp + "|"
            else:
                disp = disp + " "
        print(disp)
        # Adds row of dividing lines to separate the smaller boxes
        if(i%3 == 2 and i!=8):
            print("- - - - - - - - -")



def findEmptySpace(board:list)->(int,int):
    """
    Finds the (row, column) position of an empty space on the board (a value of 0).

    @param board: list
        List of lists representing the Sudoku board of size 9x9.

    @return
        A (row,column) position of an empty space.
        Returns (-1,-1) if nothing is empty on the board.
    """
    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col]==0):
                return (row,col)
    return (-1,-1)

def isValid(board: list, row: int, col: int, val: int) -> bool:
    """
    Checks to see if the value at the specified row and column of
    the sudoku board is valid.
    The value assigned to the specified row and column must be a
    non-zero value.

    @param board: list
        List of lists representing the Sudoku board of size 4x4.
    @param row: int
        Integer value representing the row number (0 indexed).
    @param col: int
        Integer value representing the column number (0 indexed).
    @param val: int
        Integer value of the Sudoku box

    @return
        True if value at specified position in board is valid.
        False otherwise.
    """
    assert len(board)==len(board[0])
    assert len(board)==9

    # First check the row. Make sure new assigned value does not already exist.
    for i in range(len(board)):
        if(i!=col and board[row][i] == val):
            #print("FAILED ROW")# for debugging
            return False

    # Check the column, ensuring newly assigned value doesn't already exist.
    for i in range(len(board)):
        if(i!= row and board[i][col]==val):
            #print("FAILED COL")# for debugging
            return False

    # Check the small box, ensuring newly assigned value doesn't already exist.
    # Determining the boundaries of the smaller box.
    startRow = row//3
    startCol = col//3

    startRow = startRow * 3
    startCol = startCol * 3

    stopRow = startRow + 3
    stopCol = startCol + 3

    for i in range(startRow, stopRow):
        for j in range(startCol,stopCol):
            if(i!=row and j!=col and board[i][j]==val):
                #print("FAILED BOX") # for debugging
                return False
    return True

def solve(board:list)->True:
    """
    Solves the Sudoku board.

    @param board: list
        List of lists representing the Sudoku board of size 9x9.

    @return
        True is board is solved.
        False otherwise.
    """

    row,col = findEmptySpace(board)
    # No empty spaces found
    if row==-1 or col==-1:
        return True
    # Try values 1 through 9 on this open space
    for val in range(1,10):
        # If the guess is valid, recurse
        if(isValid(board,row,col,val)):
            board[row][col] = val
            solved = solve(board)
            # If the entire board is solved, then algorithm terminates
            if(solved):
                return True
        # Guess is not valid, reset square to 0
        board[row][col] = 0
    # Exhausted all values and none of them worked
    return False

print("Given board")
printBoard(board)
print("-----------------------")
solved = solve(board)
if solved:
    print("Solution")
    printBoard(board)
else:
    print("Failed to find a solution")
