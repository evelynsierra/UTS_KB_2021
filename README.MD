# Kelompok 2 KB F
### Anggota Kelompok :
1. Bayu Eka Prawira (05111940000042)
2. Evelyn Sierra (05111940000111)

# Sudoku Solver Using Backtracking
## Penjelasan Algoritma
Algoritma yang digunakan dalam topik sudoku kali ini adalah algoritma Backtracking. Seperti halnya permasalahan Backtracking lainnya, sudoku dapat diselesaikan dengan mengisikan angka pada cell yang kosong secara satu persatu. Sebelum mengisi cell tersebut, kita harus mengecek dahulu apakah ada angka yang sama pada baris dan kolom serta subgrid 3x3 di mana cell tersebut berada. 

Setelah mengecek semua arah tersebut, kita mengisikan cell tersebut, lalu mengecek secara rekursif apakah angka tersebut sudah mengarah ke solusi atau tidak. Jika tidak, maka dicoba angka selanjutnya untuk mengisi cell tersebut (1 - 9). Namun jika tidak ada solusi, maka akan mengembalikan nilai false.

