import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    suma = 0
    for i in ar: # sirve para recorrer la matriz
        for j in i: # sirve para recorrer cada elemento de la matriz
            suma = suma + j
    print("El resultado de la suma de la siguiente matriz es de: ", suma)



if __name__ == '__main__':
    ar = [
        [1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000050, 1000000600], 
        [1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000050, 1000000600],
        [1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000050, 1000000600]]
    result = aVeryBigSum(ar)
