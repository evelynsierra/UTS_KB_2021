"""Summary
Implements a visual solution to a sudoku puzzle parsed from a file
Attributes:
    blockWidth (int): The width of each block in the table (used for scaling the graphics)
    offset (int): The amount of offset from left and right side of screen as well as between each 3x3 square
    win (TYPE): the graphics window
"""
from fileReading import *
from solvingSudoku import *
from graphics import *

blockWidth = 50
offset = 10
win = GraphWin('Sudoku', offset * 4 + blockWidth * 9 + 1, 200 + blockWidth * 9 + 1)


def drawBlock(row: int, col: int, val: int, color):
  global win
  """Summary
  Draws the given block the correct color. Also adds in the value for that block if the value is non-zero
  Args:
      row (int): row of block to draw
      col (int): col of block to draw
      val (int): value to place in the block - 0 if empty
      color (string): string to represent color for the block
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
  """Summary

  Args:
      puzzle (list): Description
      color (TYPE): Description
  """
  for row in range(9):
    for col in range(9):
      if puzzle[row][col] == 0:
        drawBlock(row, col, puzzle[row][col], 'white')
      else:
        drawBlock(row, col, puzzle[row][col], color)

def solveWithGraphics(puzzle):

  """Summary
  Solves the puzzle using recursive backtracking. Also displays its current progress to win.
  Args:
      puzzle (matrix): The puzzle to solve

  Returns:
      boolean: If the puzzle could be solved given the current status
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

      if solveWithGraphics(puzzle): # Check to see if it worked
        return True

      puzzle[row][col] = 0 # If it didn't then reset and try again
      drawBlock(row, col, 0, color_rgb(247, 169, 151))  # Draw the block red if failed
      time.sleep(0.25) # Delay
  return False

def clear(win):
    """Summary
    Clears the window of all items (undraws them)
    Args:
        win (GraphWin): the window to clear
    """
    for item in win.items[:]:
        item.undraw()
    win.update()

def rectangleContains(rect: Rectangle, p: Point):
  """Summary
  If the point given is inside of the rectange
  Args:
      rect (Rectangle): a rectangle
      p (Point): a point

  Returns:
      boolean: if the point is inside the given retangle
  """
  x = p.getX()
  y = p.getY()
  return x >= rect.getP1().getX() and x <= rect.getP2().getX() and y >= rect.getP1().getY() and y <= rect.getP2().getY()

def main():
  # Loop infinetley
  while(True):
    # Clear every time we reset
    clear(win)
    ##### Drawing the Input File Screen #######
    name = Text(Point(win.getWidth()/2, 40), "Welcome to the Sudoku Solver \n")
    instructions = Text(Point(win.getWidth()/2, win.getHeight()/2), "Then click anywhere on the screen")
    entry1 = Entry(Point(win.getWidth()/2, 200),10)
    filenamePrompt = Text(Point(win.getWidth()/2, 150),'Please type in a puzzle name and extension to begin') # label for the Entry
    beginning = [name, instructions, entry1, filenamePrompt]
    for item in beginning:
      item.draw(win)
    win.getMouse()  # To know the user is finished with the text.
    filename = entry1.getText()
    clear(win)

    ##### Getting the puzzle from the file and setting variables ######
    shouldReset = False
    blankPuzzle = getPuzzleFromFile("puzzles/" + filename)
    puzzle = getPuzzleFromFile("puzzles/" + filename)

    ##### Drawing the initial screen #######
    DrawPuzzle(blankPuzzle, "light green")
    header = Text(Point(win.getWidth() / 2, 25), "Puzzle: " + filename)
    header.setSize(24)
    header.draw(win)

    ##### Drawing the buttons at the bottom of the screen #####
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

    ##### Loop until the program should be reset #####
    while not shouldReset:
      # Wait for user input
      userInput = win.getMouse()
      print(userInput)
      if rectangleContains(solveButton, userInput): ## If the user clicks on solve
        solve(puzzle) # Solve the puzzle and then draw the puzzle on the screen in darker green
        DrawPuzzle(puzzle, color_rgb(76, 184, 46))
      elif rectangleContains(steps, userInput): ## if the user clicks on steps
        solveWithGraphics(puzzle) #Solve but showing steps
        if solve(puzzle): # If the puzzle is solveable then print it again showing that the algorithm is done
          DrawPuzzle(puzzle, color_rgb(76, 184, 46))
        else:
          DrawPuzzle(puzzle, color_rgb(247, 169, 151)) # If the algorithm is not able to find a solution then draw it in red
      elif rectangleContains(reset, userInput): # If the user clicks reset
        DrawPuzzle(blankPuzzle, "light green")  # Then draw the puzzle again in light green
        puzzle = getPuzzleFromFile("puzzles/" + filename)   # Also reset puzzle to an unsolved version
      elif rectangleContains(newFile, userInput): # If the user wants a new file
        clear(win) # Clear the window
        shouldReset = True  # Exit loop
      else:
        buttonPressed = False
  win.close()


if __name__ == '__main__':
    main()
