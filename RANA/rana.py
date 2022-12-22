import math
import os
import random
import re
import sys
#"R: Rana", "T/U: Túneles", "X: Muro", "E: Salida", "B: Bomba"
laberinto = [[' ', ' ', 'T', ' ', 'U', 'X', ' ', ' E'],
             ['R', ' ', ' ', 'X', 'X', ' ', ' ', ' '],
             [' ', ' ', 'X', 'X', 'U', ' ', ' ', 'X'],
             [' ', ' ', 'B', 'X', ' ', ' ', 'B', 'B'],
             ['T', ' ', ' ', 'X', ' ', ' ', ' ', 'E']]
intentos = 0
prob = 0
def probabilidades():
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i-1][j] == ' ' and laberinto[i][j-1] == ' ' and laberinto[i+1][j] == ' ' and laberinto[i][j+1] == ' ':
                intentos = intentos + 1
                prob = 0,75+ prob
            elif laberinto[i-1][j] == 'B' or laberinto[i][j-1] == 'B' or laberinto[i+1][j] == 'B' or laberinto[i][j+1] == 'B':
                intentos = intentos + 1
                prob = 0,25+ prob
            elif laberinto[i-1][j] == 'X' or laberinto[i][j-1] == 'X' or laberinto[i+1][j] == 'X' or laberinto[i][j+1] == 'X':
                intentos = intentos + 1
                prob = 0+ prob
            elif laberinto[i-1][j] == 'T' or laberinto[i][j-1] == 'T' or laberinto[i+1][j] == 'T' or laberinto[i][j+1] == 'T':
                intentos = intentos + 1
                prob = 0,5+ prob
            elif laberinto[i-1][j] == 'U' or laberinto[i][j-1] == 'U' or laberinto[i+1][j] == 'U' or laberinto[i][j+1] == 'U':   
                intentos = intentos + 1
                prob = 0,5+ prob
            elif laberinto[i-1][j] == 'E' or laberinto[i][j-1] == 'E' or laberinto[i+1][j] == 'E' or laberinto[i][j+1] == 'E':
                intentos = intentos + 1
                prob = 1
    print(prob/intentos)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0]) # fila
    m = int(first_multiple_input[1]) # columna
    k = int(first_multiple_input[2]) # número de movimientos
    for n_itr in range(n):
        row = input()
    for k_itr in range(k):
        second_multiple_input = input().rstrip().split()
        i1 = int(second_multiple_input[0]) # fila
        j1 = int(second_multiple_input[1]) # columna
        i2 = int(second_multiple_input[2]) # fila
        j2 = int(second_multiple_input[3]) # columna
    
    


