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

def display(grid,sudoku):
    print()
    counter = 1
    for i in range(81):
        print(sudoku[grid[i]],end =" ")
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
            
            #Removes the number from the rows
            for i in range(1,10):
                currentRow = row+str(i)
                if(len(sudoku[currentRow]))>1:
                    sudoku[currentRow] = sudoku[currentRow].replace(value," ")

            #Removes the number from the columns
            rows = ["Dummy","A","B","C","D","E","F","G","H","I"]
            for i in range(1,10):
                currentColumn = rows[i]+column
                if len(sudoku[currentColumn])>1:
                    sudoku[currentColumn] = sudoku[currentColumn].replace(value," ")

            #Remove the number from the 3*3 mini-grids in the sudoku
            if row == "A" or row == "B" or row == "C":
                minigrid_row="ABC"
            elif row == "D" or row == "E" or row == "F":
                minigrid_row="DEF"
            elif row == "G" or row == "H" or row == "I":
                minigrid_row="GHI"

            if column == "1" or column == "2" or column == "3":
                minigrid_column="123"
            elif column == "4" or column == "5" or column == "6":
                minigrid_column="456"
            elif column == "7" or column == "8" or column == "9":
                minigrid_column="789"   

            mini_grids= createGrid(minigrid_row,minigrid_column)

            for i in range(9):
                if len(sudoku[mini_grids[i]])>1:
                    sudoku[mini_grids[i]] = sudoku[mini_grids[i]].replace(value," ")

    #for loop to remove all the trailing spaces
    for i in range(81):
        sudoku[grid[i]] = sudoku[grid[i]].replace(" ","")
    return sudoku




def main():
    rows = 'ABCDEFGHI'
    cols = '123456789'

    grid = createGrid(rows, cols) 
    # Create a grid from A1 to I9

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