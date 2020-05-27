from UtilityFunctions import *
from SolutionFunctions import *

def main():
    rows = 'ABCDEFGHI'
    cols = '123456789'

    grid = createGrid(rows, cols) 
    # Create a grid from A1 to I9

    #sudokuString = input("Enter the sudoku in a string format")
    sudokuString = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
    sudokuString2 = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
    sudoku = createDict(grid,sudokuString) 
    #Creates a dictionary with location on the grid corresponding to its current value  
    
    while True:

        oldsudoku = dict(sudoku)
        sudoku = EliminateSolution(grid,sudoku)
        sudoku = OnlyOptionSolution(grid,sudoku)

        if oldsudoku == sudoku:
            if solved(grid,sudoku) == "solved":
                display(grid,sudoku)
                break
            else:
                break

    SearchSolution(grid,sudoku)            
    #display(grid,sudoku)        
if __name__ == "__main__":
    main()


