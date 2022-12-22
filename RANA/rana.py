import math
import os
import random
import re
import sys
print('\n',"R: Rana", '\n', "T/U: Túneles", '\n', "X: Muro", '\n', "E: Salida", '\n', "B: Bomba")
laberinto = [[' ', ' ', 'T', ' ', 'U', 'X', ' ', ' E'],
             ['R', ' ', ' ', 'X', 'X', ' ', ' ', ' '],
             [' ', ' ', 'X', 'X', 'U', ' ', ' ', 'X'],
             [' ', ' ', 'B', 'X', ' ', ' ', 'B', 'B'],
             ['T', ' ', ' ', 'X', ' ', ' ', ' ', 'E']]
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0]) # fila
    m = int(first_multiple_input[1]) # columna
    k = int(first_multiple_input[2]) # número de movimientos
    for n_itr in range(n):
        row = input()
# Write your code here
    for k_itr in range(k):
        second_multiple_input = input().rstrip().split()
        i1 = int(second_multiple_input[0]) # fila
        j1 = int(second_multiple_input[1]) # columna
        i2 = int(second_multiple_input[2]) # fila
        j2 = int(second_multiple_input[3]) # columna
# Write your code here
# Write your code here

