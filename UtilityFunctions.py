def printBoard(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -") #After every third row , it will print this to visually
                                           #seperate grids
        
        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j !=0: #After every third element , it will print a line
                print("| ", end="")

            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="") #After every element , a space will be printed

def findEmptySpot(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)  #Return the row and column for the empty space

    return None

def isValid(sudoku, value, position):
    # Check if value is present in the row
    for i in range(len(sudoku[0])):
        if sudoku[position[0]][i] == value and position[1] != i:
            return False

    # Check if value is presebt in the column
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == value and position[0] != i:
            return False

    # Check if the value is in the 3*3 mini-grid
    mini_grid_x = position[1] // 3
    mini_grid_y = position[0] // 3

    for i in range(mini_grid_y*3, mini_grid_y*3 + 3):
        for j in range(mini_grid_x * 3, mini_grid_x*3 + 3):
            if sudoku[i][j] == value and (i,j) != position:
                return False

    return True
