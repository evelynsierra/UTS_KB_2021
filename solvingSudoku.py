"""Summary
Contains a basic algorithm for solving sudokus. Implements recursive backtracking.
"""
from fileReading import *
import numpy as np


def canPlace(puzzle, y: int, x: int, value: int):
    """Summary
    If the given puzzle can accept the value at the postion specified

    Args:
        puzzle (matrix): The puzzle we are solving
        y (int): the row of the slot in question
        x (int): the column of the slot in question
        value (int): The value we are attempting to insert

    Returns:
        TYPE: Whether or not the item can be placed in that spot
    """
    # print(puzzle[y][x])
    if puzzle[y][x] != 0:
        #print("Space is not 0")
        return False
    # Check the row
    row = puzzle[y]
    # print(row)
    if value in puzzle[y]:
        return False
    # Check the column
    col = [line[x] for line in puzzle]
    # print(col)
    if value in col:
        return False
    boxY = y // 3
    #print(boxY)
    boxX = x // 3
    #print(boxX)
    for i in range(boxY * 3, boxY * 3 + 3):
        # print(puzzle[i][boxX * 3:boxX * 3 + 3])
        if value in puzzle[i][boxX * 3:boxX * 3 + 3]:
            return False
    return True


def solve(puzzle):
    """Summary

  Args:
      puzzle (matrix): The puzzle to solve

  Returns:
      bool: if the puzzle was solvable with the current state
  """
    firstEmpty = findNextEmpty(puzzle)
    if not firstEmpty:  # If there are no empty spots left
        return True
    row, col = firstEmpty
    for val in range(1, 10):
        if canPlace(puzzle, row, col, val):
            puzzle[row][col] = val

            if solve(puzzle):
                return True

            puzzle[row][col] = 0

    return False


def findNextEmpty(puzzle):
    """Summary

  Args:
      puzzle (matrix): The puzzle to parse

  Returns:
      TYPE: Returns the next empty item in the matrix as a tuple
  """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return (row, col)
    return None
