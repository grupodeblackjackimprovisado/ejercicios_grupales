import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    suma = 0
    for i in range(len(ar)):
        suma = suma + ar[i]
    print("El resultado de la suma de la siguiente matriz es de: ", suma)



if __name__ == '__main__':
    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000050, 1000000600]
    result = aVeryBigSum(ar)
