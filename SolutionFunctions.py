from UtilityFunctions import *

#Eliminate the numbers from their row,column and grid to reduce the
#calculations needed to solve the sudoku
def EliminateSolution(grid,sudoku):
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


#If any tile only has 1 possible outcome compared to the others in the same 3*3 grid
#this function will solve that
def OnlyOptionSolution(grid , sudoku):
 
    grid_rows = ["ABC","DEF","GHI"]
    grid_column = ["123","456","789"]

    for a in range(3):
        for b in range(3):
            #Start creating from top-left grid to bottom-right
            mini_grids= createGrid(grid_rows[a],grid_column[b])
            flag = 0 

            for i in range(9):
                if len(sudoku[mini_grids[i]])>1:
                    flag+=1
            #If all the values in the grid are single values , that grid
            #wont be calculated

            if flag !=0:
                for z in range(9):
                    findUnique = ""
                    for i in range(9):
                        if len(sudoku[mini_grids[i]])>1:
                            findUnique = findUnique + sudoku[mini_grids[i]]
                            #Combine all the positions that can have more than 
                            # 1 possible outcome

                    findUnique = findDistinct(findUnique)
                    findUniqueList = findUnique.split()
                    #Creates a list of all the numbers that only appear once per grid

                    for j in range(len(findUniqueList)):
                        for i in range(9):
                            if len(sudoku[mini_grids[i]])>1 and findUniqueList[j] in sudoku[mini_grids[i]]:
                                sudoku[mini_grids[i]] = sudoku[mini_grids[i]].replace(sudoku[mini_grids[i]],findUniqueList[j])    
                                #Replace the string of possible outcomes with the unique number that fits over there
                    findUnique = []

    return sudoku

def SearchSolution(grid,sudoku):

    possibleValues = []
    counter = 0
    for i in range(80):
        if len(sudoku[grid[i]])>1:

            for j in range(len(sudoku[grid[i]])):
                possibleValues.append(sudoku[grid[i]][j])

            for k in range(len(possibleValues)):
                copysudoku = dict(sudoku)
                copysudoku[grid[i]] = possibleValues[k]
    
                for x in range(80):
                    copysudoku = EliminateSolution(grid,copysudoku)
                    copysudoku = OnlyOptionSolution(grid,copysudoku)

                    solvedOrNot = solved(grid,copysudoku)
                    print(solvedOrNot)
                    
                    if solvedOrNot == "solved":
                        print("hello")
                        return copysudoku
                    print(counter)
                    counter+=1

            possibleValues = []























    # grid_rows = ["ABC","DEF","GHI"]
    # grid_column = ["123","456","789"]
    # allOutcomesList = []
    # allOutcomesCurrent = []

    # #Store all the locations where more than 1 number can be placed
    # for a in range(3):
    #     for b in range(3):
    #         #Start creating from top-left grid to bottom-right
    #         mini_grids= createGrid(grid_rows[a],grid_column[b])

    #         for i in range(9):
    #             if len(sudoku[mini_grids[i]])>1:
    #                 allOutcomesCurrent.append(sudoku[mini_grids[i]])
    #         allOutcomesList.append(allOutcomesCurrent)
    #         allOutcomesCurrent = []
            
            
