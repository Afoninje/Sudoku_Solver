from Functions import *
from SolutionFunctions import *

def main():
    rows = 'ABCDEFGHI'
    cols = '123456789'

    grid = createGrid(rows, cols) 
    # Create a grid from A1 to I9

    #sudokuString = input("Enter the sudoku in a string format")
    sudokuString = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
    sudoku = createDict(grid,sudokuString) 

    #Creates a dictionary with location on the grid corresponding to its current value  
    
    while True:
        sudoku = eliminate(grid,sudoku)
        sudoku = onlyOption(grid,sudoku)
        solvedOrNot = solved(grid,sudoku)

        if solvedOrNot == "solved":
            display(grid,sudoku)
            break

if __name__ == "__main__":
    main()


