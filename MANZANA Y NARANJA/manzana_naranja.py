import math
import os
import random
import re
import sys
#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
# 1. INTEGER s
# 2. INTEGER t
# 3. INTEGER a
# 4. INTEGER b
# 5. INTEGER_ARRAY apples
# 6. INTEGER_ARRAY oranges
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    
# Write your code here
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0]) # inicio de la casa
    t = int(first_multiple_input[1]) # fin de la casa
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0]) # posicion de la manzana
    b = int(second_multiple_input[1]) # posicion de la naranja
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0]) # numero de manzanas
    n = int(third_multiple_input[1]) # numero de naranjas
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
