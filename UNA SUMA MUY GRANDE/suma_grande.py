#/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'aVeryBigSum' function below.

# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.

def aVeryBigSum(ar):
    suma = 0 #Definir la variable suma
    # Write your code here
    for i in range(len(ar)): #Recorrer la matriz
        suma = suma + ar[i] #Sumar los elementos de la matriz
    print("El resultado de la suma de la siguiente matriz es de: ", suma)



# Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip()) #ar_count = 5
    ar = list(map(int, input().rstrip().split())) #Escribir la matriz de números separados por espacios en una lista
    result = aVeryBigSum(ar) #Llamar a la función
    fptr.write(str(result) + '\n')
    fptr.close()
