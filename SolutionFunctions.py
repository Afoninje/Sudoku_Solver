from Functions import *
def eliminate(grid,sudoku):
    for i in range(81):
        if len(sudoku[grid[i]]) == 1:
            value = sudoku[grid[i]]
            row = grid[i][0]
            column = grid[i][1]
            
            #Replace the number from the rows with a space
            for i in range(1,10):
                currentRow = row+str(i)
                if(len(sudoku[currentRow]))>1:
                    sudoku[currentRow] = sudoku[currentRow].replace(value," ")

            #Replace the number from the columns with a space
            rows = ["Dummy","A","B","C","D","E","F","G","H","I"]
            for i in range(1,10):
                currentColumn = rows[i]+column
                if len(sudoku[currentColumn])>1:
                    sudoku[currentColumn] = sudoku[currentColumn].replace(value," ")

            #Replace the number from the 3*3 mini-grids with a space
            if row in "ABC":
                minigrid_row="ABC"
            if row in "DEF":
                minigrid_row="DEF"
            if row in "GHI":
                minigrid_row="GHI"

            if column in "123":
                minigrid_column="123"
            if column in "456":
                minigrid_column="456"
            if column in "789":
                minigrid_column="789"   

            mini_grids= createGrid(minigrid_row,minigrid_column)

            for i in range(9):
                if len(sudoku[mini_grids[i]])>1:
                    sudoku[mini_grids[i]] = sudoku[mini_grids[i]].replace(value," ")

    #for loop to remove all the trailing spaces
    for i in range(81):
        sudoku[grid[i]] = sudoku[grid[i]].replace(" ","")
    return sudoku



def onlyOption(grid , sudoku):
    #If any tile only has 1 possible outcome compared to the others in the same 3*3 grid
    #this function will solve that

    grid_rows = ["ABC","DEF","GHI"]
    grid_column = ["123","456","789"]

    for a in range(3):
        for b in range(3):
            mini_grids= createGrid(grid_rows[a],grid_column[b])
            flag = 0 

            for i in range(9):
                if len(sudoku[mini_grids[i]])>1:
                     flag+=1

            if flag !=0:
                for z in range(9):
                    findUnique = ""
                    for i in range(9):
                        if len(sudoku[mini_grids[i]])>1:
                            findUnique = findUnique + sudoku[mini_grids[i]]

                    findUnique = findDistinct(findUnique)
                    findUniqueList = findUnique.split()


                    for j in range(len(findUniqueList)):
                        for i in range(9):
                            if len(sudoku[mini_grids[i]])>1 and findUniqueList[j] in sudoku[mini_grids[i]]:
                                sudoku[mini_grids[i]] = sudoku[mini_grids[i]].replace(sudoku[mini_grids[i]],findUniqueList[j])    
                    findUnique = []

    return sudoku
