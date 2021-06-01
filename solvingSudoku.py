"""
Algoritma Backtracking menyelesaikan sudoku
"""
from fileReading import *
import numpy as np

"""
Cek apakah kotak boleh diisi
"""
def canPlace(puzzle, y: int, x: int, value: int):
    """
        y (int): baris
        x (int): kolom
        value (int): angka yang akan dimasukkan
    """
    # Jika puzzle tidak kosong, return false
    if puzzle[y][x] != 0:
        return False
    
    # cek baris
    row = puzzle[y]
    
    # print(baris)
    if value in puzzle[y]:
        return False
    
    # cek kolom
    col = [line[x] for line in puzzle]
    
    # print(kolom)
    if value in col:
        return False
    
    boxY = y // 3
    
    #print(box Y)
    boxX = x // 3
    
    #print(box X)
    for i in range(boxY * 3, boxY * 3 + 3):
        
        # print
        if value in puzzle[i][boxX * 3:boxX * 3 + 3]:
            return False
    return True


def solve(puzzle):
    """
    Solve puzzle dan return bool
  """
    firstEmpty = findNextEmpty(puzzle)
    if not firstEmpty:  # Jika ada yang kosong
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
    """
    Cari kotak yang kosong selanjutnya
  """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return (row, col)
    return None
