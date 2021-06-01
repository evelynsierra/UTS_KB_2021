def getPuzzleFromFile(fileName: str):
  """
  Membuat matriks 9x9 dari file yang telah dibuat
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
  """
  Print ke sudokugraphic
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


