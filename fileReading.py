def getPuzzleFromFile(fileName: str):
  """Summary
  Creates a 9x9 matrix from the given file
  Args:
      fileName (str): the filename for the file given
  """
  f = open(fileName, "r")
  puzzle = []
  for i in range(9):
    line = f.readline()
    lineArray = [int(c) for c in line if not (c == ' ' or c == '\n')]
    puzzle.append(lineArray)
  # printSudoku(puzzle)
  return puzzle

def printSudoku(puzzle):
  """Summary
  Prints a 9x9 grid of numbers into a sudoku board, better than np.matrix
  Args:
      puzzle (matrix): The board to be printed
  """
  for i in range(9):
    for j in range(9):
      if (j + 1) % 3 == 0:
        print(puzzle[i][j], end ="|")
      else:
        print(puzzle[i][j], end =" ")
    if (i + 1) % 3 == 0 and i != 8:
      print("\n-------------------")
    else:
      print("")


