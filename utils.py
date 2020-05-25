def createGrid(a, b):
      return [s+t for s in a for t in b]

def createDict(grid,sudokuString):
    counter = 0
    sudokuDict = {}
    for i in sudokuString:
        if i == ".":
            sudokuDict[grid[counter]] = "123456789"
        else:
            sudokuDict[grid[counter]] = i

        counter +=1

    return sudokuDict

def display(grid,sudokuDict):
    print()
    counter = 1
    for i in range(81):
        print(sudokuDict[grid[i]],end =" ")
        if counter%9==0:
            print()
        elif counter%3==0:
            print("|",end=" ")
        
        if counter%27==0:
            print("------+-------+-------")
       
        if counter<80:
            counter +=1

def eliminate(grid,sudoku):
    for i in range(81):
        if len(sudoku[grid[i]]) == 1:
            value = sudoku[grid[i]]
            row = grid[i][0]
            column = grid[i][1]
            
            for i in range(1,10):
                currentRow = row+str(i)
                if(len(sudoku[currentRow]))>1:
                    print(currentRow,value)
                    sudoku[currentRow] = sudoku[currentRow].replace(value,"")

            rows = ["Dummy","A","B","C","D","E","F","G","H","I"]
            for i in range(1,10):
                currentColumn = rows[i]+column
                if(len(sudoku[currentColumn]))>1:
                    sudoku[currentColumn] = sudoku[currentColumn].replace(value,"")

    return sudoku




def main():
    rows = 'ABCDEFGHI'
    cols = '123456789'

    grid = createGrid(rows, cols) 
    # Create a grid from A1 to I9
    row_units = [createGrid(r, cols) for r in rows] 
    # Create row. Ex = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
    column_units = [createGrid(rows, c) for c in cols] 
    # Create column. Ex = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
    square_units = [createGrid(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')] 
    # Create the sub-grids. Ex = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

    #sudokuString = input("Enter the sudoku in a string format")
    sudokuString = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
    sudoku = createDict(grid,sudokuString) 

    #Creates a dictionary with location on the grid corresponding to its current value  
    
    #display(grid,sudoku) 

    sudoku = eliminate(grid,sudoku)

    display(grid,sudoku) 


if __name__ == "__main__":
    main()


#..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..