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
Starting with a simple Sudoku board as a warm up.
"""
board = [[1,0,3,0],
        [0,0,1,4],
        [4,1,0,0],
        [0,3,0,0]]

def resetBoard(board: list):
    """
    Resets the board to its original values.

    @param board:list
        List of lists representing the Sudoku board of size 4x4.
    """
    board = [[1,0,3,0],
            [0,0,1,4],
            [4,1,0,0],
            [0,3,0,0]]


def printBoard(board: list):
    """
    Prints the Sudoku board in a user friendly way in the output box.

    @param board:list
        List of lists representing the Sudoku board of size 4x4.
    """
    for i in range(len(board)):
        row = board[i]
        disp = ""
        # Displays each element in the row, adding vertical bar where necessary
        for j in range(len(row)):
            item = row[j]
            disp = disp+str(item)
            # for the smaller sub boxes
            if(j == 1):
                disp = disp + "|"
            else:
                disp = disp + " "
        print(disp)
        # Adds row of dividing lines to separate the smaller boxes
        if(i == 1):
            print("- - - - ")



def findEmptySpace(board:list)->(int,int):
    """
    Finds the (row, column) position of an empty space on the board (a value of 0).

    @param board: list
        List of lists representing the Sudoku board of size 4x4.

    @return
        A (row,column) position of an empty space.
        Returns (-1,-1) if nothing is empty on the board.
    """
    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col]==0):
                return (row,col)
    return (-1,-1)

def isValid(board: list, row: int, col: int) -> bool:
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

    @return
        True if value at specified position in board is valid.
        False otherwise.
    """
    assert len(board)==len(board[0])
    assert len(board)==4

    currVal = board[row][col]
    # First check the row. Make sure new assigned value does not already exist.
    for i in range(len(board)):
        if(i!=col and board[row][i] == currVal):
            #print("FAILED ROW")# for debugging
            return False

    # Check the column, ensuring newly assigned value doesn't already exist.
    for i in range(len(board)):
        if(i!= row and board[i][col]==currVal):
            #print("FAILED COL")# for debugging
            return False

    # Check the small box, ensuring newly assigned value doesn't already exist.
    # Determining the boundaries of the smaller box.
    startRow = 0
    startCol = 0

    if row > 1:
        startRow = 2
    if col > 1:
        startCol = 2

    stopRow = startRow + 2
    stopCol = startCol + 2

    for i in range(startRow, stopRow):
        for j in range(startCol,stopCol):
            if(i!=row and j!=col and board[i][j]==currVal):
                #print("FAILED BOX") # for debugging
                return False
    return True

def solve(board:list)->True:
    """
    Solves the Sudoku board.

    @param board: list
        List of lists representing the Sudoku board of size 4x4.

    @return
        True is board is solved.
        False otherwise.
    """

    row,col = findEmptySpace(board)
    # No empty spaces found
    if row==-1 or col==-1:
        return True
    # Try values 1 through 4 on this open space
    for val in range(1,5):
        board[row][col] = val
        # If the guess is valid, recurse
        if(isValid(board,row,col)):
            solved = solve(board)
            # If the entire board is solved, then algorithm terminates
            if(solved):
                return True
        # Guess is not valid, reset square to 0
        else:
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
