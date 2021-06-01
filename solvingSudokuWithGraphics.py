from fileReading import *
from solvingSudoku import *
from graphics import *

"""
  blockWidth (int): lebar dari setiap block
    offset (int): offset kiri kanan layar dari block
    win (TYPE): window graphic 
"""
blockWidth = 50
offset = 10
win = GraphWin('Sudoku', offset * 4 + blockWidth * 9 + 1, 200 + blockWidth * 9 + 1)


def drawBlock(row: int, col: int, val: int, color):
  global win
  """
      row (int): baris
      col (int): kolom
      val (int): nilai untuk dimasukkan saat kotak kosong
      color (string): untuk warna
  """
  verticalOffsets = row // 3 + 1
  verticalO = verticalOffsets * offset + 50
  horizontalOffsets = col // 3 + 1
  horizontalO = horizontalOffsets * offset
  upperLeft = Point(col * blockWidth, row * blockWidth)
  upperLeft.move(horizontalO, verticalO)
  bottomRight = Point((col + 1) * blockWidth, (row + 1) * blockWidth)
  bottomRight.move(horizontalO, verticalO)
  block = Rectangle(upperLeft, bottomRight)
  block.setFill(color)
  block.draw(win)

  if val != 0:
    textPoint = Point(col * blockWidth + blockWidth/2, row * blockWidth + blockWidth/2)
    textPoint.move(horizontalO, verticalO)
    numberImage = Text(textPoint, str(val))
    numberImage.draw(win)


def DrawPuzzle(puzzle: list, color):
  """
  Untuk menampilkan puzzle
  """
  for row in range(9):
    for col in range(9):
      if puzzle[row][col] == 0:
        drawBlock(row, col, puzzle[row][col], 'white')
      else:
        drawBlock(row, col, puzzle[row][col], color)

def solveWithGraphics(puzzle):

  """
  Menggunakan algoritma backtracking untuk menyelesaikan puzzle
  """
  time.sleep(0.25)
  firstEmpty = findNextEmpty(puzzle) # Find the next empty spot
  if not firstEmpty: # If there are no empty spots left
    return True
  row, col = firstEmpty
  for val in range(1, 10):
    if canPlace(puzzle, row, col, val):
      puzzle[row][col] = val
      drawBlock(row, col, val, "light gray")

      if solveWithGraphics(puzzle): # untuk pengecekan apakah berhasil
        return True

      puzzle[row][col] = 0 # Jika tidak reset, coba lagi
      drawBlock(row, col, 0, color_rgb(247, 169, 151))  #Block jadi merah apabil agagal
      time.sleep(0.25) # Delay
  return False

def clear(win):
    """
    Clear window
    """
    for item in win.items[:]:
        item.undraw()
    win.update()

def rectangleContains(rect: Rectangle, p: Point):
  """
  Memberikan poin ke dalam kotak
  """
  x = p.getX()
  y = p.getY()
  return x >= rect.getP1().getX() and x <= rect.getP2().getX() and y >= rect.getP1().getY() and y <= rect.getP2().getY()

def main():
  while(True):
    # bersihkan layar setiap kali reset
    clear(win)
    ##### Screen Input nama file #######
    name = Text(Point(win.getWidth()/2, 40), "Welcome to the Sudoku Solver \n")
    instructions = Text(Point(win.getWidth()/2, win.getHeight()/2), "Kemudian klik di mana pun di dalam window ini")
    entry1 = Entry(Point(win.getWidth()/2, 200),10)
    filenamePrompt = Text(Point(win.getWidth()/2, 150),'Ketik nama file input dan ekstensinya untuk mulai') #label untuk entry
    beginning = [name, instructions, entry1, filenamePrompt]
    for item in beginning:
      item.draw(win)
    win.getMouse()  # saat user telah selesai mmenuliskan tulisan
    filename = entry1.getText()
    clear(win)

    ##### Ambil puzzle dari file ######
    shouldReset = False
    blankPuzzle = getPuzzleFromFile("puzzles/" + filename)
    puzzle = getPuzzleFromFile("puzzles/" + filename)

    ##### Screen awal #######
    DrawPuzzle(blankPuzzle, "light green")
    header = Text(Point(win.getWidth() / 2, 25), "Puzzle: " + filename)
    header.setSize(24)
    header.draw(win)

    ##### Tombol di bawah screen #####
    buttonWidth = 100
    buttonHeight = 40
    solveButton = Rectangle(Point((win.getWidth() / 6) - (buttonWidth / 2), win.getHeight() - 65 - buttonHeight / 2),
                          Point(win.getWidth()/6+ buttonWidth / 2, win.getHeight() - 65 + buttonHeight / 2))
    solveText = Text(Point((win.getWidth() / 6), win.getHeight() - 65), "Solve")

    solveButton.draw(win)
    solveText.draw(win)

    steps = Rectangle(Point((win.getWidth() / 2) - (buttonWidth / 2), win.getHeight() - 65 - buttonHeight / 2), Point(win.getWidth() / 2 + (buttonWidth / 2), win.getHeight() - 65 + buttonHeight / 2))
    solveText = Text(Point((win.getWidth() / 2), win.getHeight() - 65), "Steps")

    steps.draw(win)
    solveText.draw(win)

    reset = Rectangle(Point((5 * win.getWidth() / 6) - (buttonWidth / 2), win.getHeight() - 90 - buttonHeight / 2),
                          Point(5 * win.getWidth()/ 6 + buttonWidth / 2, win.getHeight() - 90 + buttonHeight / 2))
    resetText = Text(Point((5 * win.getWidth() / 6), win.getHeight() - 90), "Reset")
    reset.draw(win)
    resetText.draw(win)

    newFile = Rectangle(Point((5 * win.getWidth() / 6) - (buttonWidth / 2), win.getHeight() - 40 - buttonHeight / 2),
                          Point(5 * win.getWidth()/ 6 + buttonWidth / 2, win.getHeight() - 40 + buttonHeight / 2))
    newFileText = Text(Point((5 * win.getWidth() / 6), win.getHeight() - 40), "New File")
    newFile.draw(win)
    newFileText.draw(win)

    ##### Ulangi terus sampai menekan reset #####
    while not shouldReset:
      # Menunggu user input
      userInput = win.getMouse()
      print(userInput)
      if rectangleContains(solveButton, userInput): ## Jika user klik tombol solve, maka puzzle akan tersolve langsung
        solve(puzzle)
        DrawPuzzle(puzzle, color_rgb(76, 184, 46))
      elif rectangleContains(steps, userInput): ## Jika user klik tombol steps, maka program akan satu per satu menyelesaikan puzzle
        solveWithGraphics(puzzle) 
        if solve(puzzle): # Jika bisa diselesaikan, maka tampilkan selesai
          DrawPuzzle(puzzle, color_rgb(76, 184, 46))
        else:
          DrawPuzzle(puzzle, color_rgb(247, 169, 151)) # Jika tidak menemukan solusi, akan muncul warna merah
      elif rectangleContains(reset, userInput): # saat user menekan reset
        DrawPuzzle(blankPuzzle, "light green")  # ulang menampilkan puzzle
        puzzle = getPuzzleFromFile("puzzles/" + filename)   # reset ke versi unsolved
      elif rectangleContains(newFile, userInput): # saat user ingin new file
        clear(win) # clear window
        shouldReset = True  # keluar loop
      else:
        buttonPressed = False
  win.close()


if __name__ == '__main__':
    main()
