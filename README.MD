# Kelompok 2 KB F
### Anggota Kelompok :
1. Bayu Eka Prawira (05111940000042)
2. Evelyn Sierra (05111940000111)

# Sudoku Solver Using Backtracking
## Penjelasan Algoritma
Algoritma yang digunakan dalam topik sudoku kali ini adalah algoritma Backtracking. Seperti halnya permasalahan Backtracking lainnya, sudoku dapat diselesaikan dengan mengisikan angka pada cell yang kosong secara satu persatu. Sebelum mengisi cell tersebut, kita harus mengecek dahulu apakah ada angka yang sama pada baris dan kolom serta subgrid 3x3 di mana cell tersebut berada. 

Setelah mengecek semua arah tersebut, kita mengisikan cell tersebut, lalu mengecek secara rekursif apakah angka tersebut sudah mengarah ke solusi atau tidak. Jika tidak, maka dicoba angka selanjutnya untuk mengisi cell tersebut (1 - 9). Namun jika tidak ada solusi, maka akan mengembalikan nilai false.

### File : solvingSudoku.py
```py
def solve(puzzle):
    """
    Solve puzzle dan return bool
  """
    firstEmpty = findNextEmpty(puzzle)
    if not firstEmpty:  # Jika tidak ada yang kosong
        return True
    row, col = firstEmpty
    for val in range(1, 10):
        if canPlace(puzzle, row, col, val):
            puzzle[row][col] = val

            if solve(puzzle):
                return True

            puzzle[row][col] = 0

    return False
```
Di dalam fungsi solve tersebut, kita mengecek dahulu apakah kotak di lokasi yang sejajar baris dan kolom, dan di dalam subgrid 3x3 sudah terisi dengan angka atau belum, jika tidak kosong maka akan mengembalikan True. Untuk mengeceknya, kita menggunakan fungsi findNextEmpty.
```py
def findNextEmpty(puzzle):
    """
    Cari kotak yang kosong selanjutnya
  """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return (row, col)
    return None
```
Kemudian, setelah mencari apakah kotak sudah bisa diletakkan angka, dilakukan perulangan. 
```py
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
```
Kemudian jika memenuhi keadaan bisa mengisi kotak tersebut, maka diisilah dengan angka dari 1 - 9 dicoba satu-satu. Jika sudah benar terisi, maka akan mereturn True namun jika masih belum, maka kotak akan dikosongkan kembali dan mencoba dengan angka yang lain. Jika tidak mungkin ada hasil, maka akan mengembalikan False.