#Return the unique values for a grid
def findDistinct(Str): 

    n = len(Str) 
    unique = ""
    count = [0 for i in range(256)] 
    index = [n for i in range(256)] 

    for i in range(n): 

        x = ord(Str[i]) 
        count[x] += 1
 
        if (count[x] == 1 and x !=' '): 
            index[x] = i 
 
        if (count[x] == 2): 
            index[x] = n 
            
    index=sorted(index) 
  
    for i in range(256): 
        if index[i] == n: 
            break
        unique = unique + Str[index[i]] 

    return unique

#Create grid by supplying row and column
def createGrid(a, b):
      return [s+t for s in a for t in b]

#Create dictionary which holds position on the grid as the key
#and the number on the position as the value
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

#Display the sudoku in a easy to read manner
def display(grid,sudoku):
    
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

#Check if the sudoku is solved in its current state
def solved(grid,sudoku):
    flag=0
    for i in range(81):
        if len(sudoku[grid[i]])>1:
            flag+=1
        
    if flag == 0:
        return "solved"
    else:
        return "notsolved"