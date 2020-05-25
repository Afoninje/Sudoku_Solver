rows = 'ABCDEFGHI'
cols = '123456789'

def createGrid(a, b):
      return [s+t for s in a for t in b]

def createDict(sudokuString):
    grid = createGrid(rows, cols) 
    counter = 0
    sudokuDict = {}
    for i in sudokuString:
        sudokuDict[grid[counter]] = i
        counter +=1

    return sudokuDict

def display(grid,sudokuDict):
    counter = 1
    for i in range(81):
        print(sudokuDict[grid[i]],end =" ")
        if counter%9==0:
            print()
        elif counter%3==0:
            print("|",end=" ")
        
        if counter%27==0:
            print("------+-------+-------")
       
        counter +=1



def main():
    grid = createGrid(rows, cols) 
    # Create a grid from A1 to I9
    row_units = [createGrid(r, cols) for r in rows] 
    # Create row. Ex = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
    column_units = [createGrid(rows, c) for c in cols] 
    # Create column. Ex = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
    square_units = [createGrid(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')] 
    # Create the sub-grids. Ex = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    unitlist = row_units + column_units + square_units
    # Combine all of them to later check the solution against each element

    sudokuString = input("Enter the sudoku in a string format")
    sudoku = createDict(sudokuString)
  
    display(grid,sudoku) 

if __name__ == "__main__":
    main()